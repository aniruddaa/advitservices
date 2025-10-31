#!/usr/bin/env bash
# diagnose_and_fix_k8s.sh
# Usage: ./diagnose_and_fix_k8s.sh <namespace> <deployment-name>
# Requires: kubectl configured for the target cluster and context

set -euo pipefail
NAMESPACE=${1:-default}
DEPLOYMENT=${2:-advitservices}
# Optional: container name if multi-container pod
CONTAINER=${3:-}

echo "Namespace: $NAMESPACE"
echo "Deployment: $DEPLOYMENT"

echo "Listing pods for deployment..."
kubectl get pods -n "$NAMESPACE" -l app.kubernetes.io/name="$DEPLOYMENT" -o wide || kubectl get pods -n "$NAMESPACE"

# Pick a pod to inspect
POD=$(kubectl get pods -n "$NAMESPACE" -l app.kubernetes.io/name="$DEPLOYMENT" -o jsonpath='{.items[0].metadata.name}' 2>/dev/null || true)
if [ -z "$POD" ]; then
  echo "No pod found with label app.kubernetes.io/name=$DEPLOYMENT; listing pods in namespace:"
  kubectl get pods -n "$NAMESPACE"
  exit 1
fi

echo "Selected pod: $POD"

echo "Collecting recent pod logs (last 500 lines)..."
if [ -n "$CONTAINER" ]; then
  kubectl logs -n "$NAMESPACE" "$POD" -c "$CONTAINER" --tail=500 || true
else
  kubectl logs -n "$NAMESPACE" "$POD" --tail=500 || true
fi

echo "Describing pod for events and status..."
kubectl describe pod -n "$NAMESPACE" "$POD" | sed -n '1,200p'

# Try running migrations inside the pod (safe attempt)
# This assumes the container image includes the manage.py and python binary.
read -p "Run migrations inside the pod? [y/N]: " run_migrate
if [[ "$run_migrate" =~ ^[Yy]$ ]]; then
  echo "Attempting to run migrations inside the pod..."
  if [ -n "$CONTAINER" ]; then
    kubectl exec -n "$NAMESPACE" -it "$POD" -c "$CONTAINER" -- /bin/sh -c 'python manage.py migrate --noinput'
    kubectl exec -n "$NAMESPACE" -it "$POD" -c "$CONTAINER" -- /bin/sh -c 'python manage.py collectstatic --noinput'
  else
    kubectl exec -n "$NAMESPACE" -it "$POD" -- /bin/sh -c 'python manage.py migrate --noinput'
    kubectl exec -n "$NAMESPACE" -it "$POD" -- /bin/sh -c 'python manage.py collectstatic --noinput'
  fi
fi

read -p "Restart the deployment to recreate pods? [y/N]: " do_restart
if [[ "$do_restart" =~ ^[Yy]$ ]]; then
  echo "Restarting deployment $DEPLOYMENT in namespace $NAMESPACE"
  kubectl rollout restart deployment/$DEPLOYMENT -n "$NAMESPACE"
  echo "Waiting for rollout to finish..."
  kubectl rollout status deployment/$DEPLOYMENT -n "$NAMESPACE"
fi

echo "Fetching recent events (sorted)..."
kubectl get events -n "$NAMESPACE" --sort-by='.lastTimestamp' | tail -n 200

echo "Done. Review logs above for errors (tracebacks, DB connection errors, DisallowedHost, etc.)."