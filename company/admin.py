from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'industry', 'location', 'company_size', 'is_verified')
    list_filter = ('is_verified', 'industry', 'company_size')
    search_fields = ('name', 'description', 'location', 'industry')
    actions = ['verify_companies']

    def verify_companies(self, request, queryset):
        queryset.update(is_verified=True)
    verify_companies.short_description = "Mark selected companies as verified"
