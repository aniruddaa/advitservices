from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    website = models.URLField(blank=True)
    logo = models.ImageField(default='company_default.jpg', upload_to='company_logos')
    location = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    founded_year = models.PositiveIntegerField()
    company_size = models.CharField(max_length=50, choices=[
        ('1-10', '1-10 employees'),
        ('11-50', '11-50 employees'),
        ('51-200', '51-200 employees'),
        ('201-500', '201-500 employees'),
        ('501+', '501+ employees')
    ])
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Companies'
