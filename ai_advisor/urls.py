from django.urls import path
from . import views

app_name = 'ai_advisor'

urlpatterns = [
    path('dashboard/', views.ai_dashboard, name='dashboard'),
    path('preferences/', views.update_preferences, name='preferences'),
]