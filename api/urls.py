# api/urls.py

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (
    RoleViewSet, UserViewSet, ServiceViewSet, VehicleViewSet, AppointmentViewSet, ServiceDetailViewSet,
    register_user, login_user, logout_user
)

# Создаем роутер и регистрируем наши ViewSet
router = DefaultRouter()
router.register(r'roles', RoleViewSet)
router.register(r'users', UserViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'vehicles', VehicleViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'service-details', ServiceDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
