from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Job, JobApplication
from .forms import JobPostForm, JobApplicationForm
from company.models import Company

def job_list(request):
    jobs = Job.objects.filter(is_active=True).order_by('-posted_date')
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    already_applied = False
    if request.user.is_authenticated:
        already_applied = JobApplication.objects.filter(job=job, applicant=request.user).exists()
    return render(request, 'jobs/job_detail.html', {'job': job, 'already_applied': already_applied})

@login_required
def job_apply(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if JobApplication.objects.filter(job=job, applicant=request.user).exists():
        messages.warning(request, 'You have already applied for this job.')
        return redirect('job-detail', pk=pk)
    
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user
            application.save()
            messages.success(request, 'Your application has been submitted successfully!')
            return redirect('job-detail', pk=pk)
    else:
        form = JobApplicationForm()
    return render(request, 'jobs/job_apply.html', {'form': form, 'job': job})

@login_required
def post_job(request):
    try:
        company = request.user.company
    except Company.DoesNotExist:
        messages.error(request, 'You need to create a company profile first.')
        return redirect('company-register')
    
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = company
            job.save()
            messages.success(request, 'Job posted successfully!')
            return redirect('job-detail', pk=job.pk)
    else:
        form = JobPostForm()
    return render(request, 'jobs/post_job.html', {'form': form})

@login_required
def application_list(request):
    if hasattr(request.user, 'company'):
        # For employers
        jobs = Job.objects.filter(company=request.user.company)
        applications = JobApplication.objects.filter(job__in=jobs)
    else:
        # For job seekers
        applications = JobApplication.objects.filter(applicant=request.user)
    return render(request, 'jobs/application_list.html', {'applications': applications})

@login_required
def update_application_status(request, pk):
    application = get_object_or_404(JobApplication, pk=pk)
    if request.user != application.job.company.user:
        messages.error(request, 'You are not authorized to perform this action.')
        return redirect('application-list')
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(JobApplication._meta.get_field('status').choices):
            application.status = new_status
            application.save()
            messages.success(request, f'Application status updated to {new_status}.')
        else:
            messages.error(request, 'Invalid status provided.')
    return redirect('application-list')
