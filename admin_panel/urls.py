from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='admin_login'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
]