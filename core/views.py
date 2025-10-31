from django.shortcuts import render
from jobs.models import Job
from company.models import Company

def home(request):
    latest_jobs = Job.objects.filter(is_active=True).order_by('-posted_date')[:5]
    featured_companies = Company.objects.filter(is_verified=True)[:4]
    context = {
        'latest_jobs': latest_jobs,
        'featured_companies': featured_companies
    }
    return render(request, 'core/home.html', context)

def about(request):
    return render(request, 'core/about.html')
