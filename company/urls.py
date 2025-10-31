from django.urls import path
from . import views

urlpatterns = [
    path('', views.company_list, name='company-list'),
    path('<int:pk>/', views.company_detail, name='company-detail'),
    path('register/', views.company_register, name='company-register'),
    path('update/', views.company_update, name='company-update'),
]