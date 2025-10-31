from django import forms
from .models import Company

class CompanyRegistrationForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'description', 'website', 'logo', 'location', 
                 'industry', 'founded_year', 'company_size']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'founded_year': forms.NumberInput(attrs={'min': 1800, 'max': 2100}),
        }