from django.contrib import admin
from .models import Job, JobApplication

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'job_type', 'posted_date', 'is_active')
    list_filter = ('is_active', 'job_type', 'company')
    search_fields = ('title', 'description', 'requirements', 'location')
    date_hierarchy = 'posted_date'

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'applicant', 'applied_date', 'status')
    list_filter = ('status', 'applied_date')
    search_fields = ('job__title', 'applicant__username', 'cover_letter')
