from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Company
from .forms import CompanyRegistrationForm
from jobs.models import Job

def company_list(request):
    companies = Company.objects.filter(is_verified=True)
    return render(request, 'company/company_list.html', {'companies': companies})

def company_detail(request, pk):
    company = get_object_or_404(Company, pk=pk)
    jobs = Job.objects.filter(company=company, is_active=True)
    return render(request, 'company/company_detail.html', {
        'company': company,
        'jobs': jobs
    })

@login_required
def company_register(request):
    try:
        company = request.user.company
        messages.warning(request, 'You already have a registered company.')
        return redirect('company-detail', pk=company.pk)
    except Company.DoesNotExist:
        pass

    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            company = form.save(commit=False)
            company.user = request.user
            company.save()
            messages.success(request, 'Company profile created successfully!')
            return redirect('company-detail', pk=company.pk)
    else:
        form = CompanyRegistrationForm()
    return render(request, 'company/company_register.html', {'form': form})

@login_required
def company_update(request):
    try:
        company = request.user.company
    except Company.DoesNotExist:
        messages.error(request, 'You need to create a company profile first.')
        return redirect('company-register')

    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            messages.success(request, 'Company profile updated successfully!')
            return redirect('company-detail', pk=company.pk)
    else:
        form = CompanyRegistrationForm(instance=company)
    return render(request, 'company/company_update.html', {'form': form})
