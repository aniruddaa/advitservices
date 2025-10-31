from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job-list'),
    path('<int:pk>/', views.job_detail, name='job-detail'),
    path('<int:pk>/apply/', views.job_apply, name='job-apply'),
    path('post/', views.post_job, name='post-job'),
    path('applications/', views.application_list, name='application-list'),
    path('applications/<int:pk>/update/', views.update_application_status, name='update-application'),
]