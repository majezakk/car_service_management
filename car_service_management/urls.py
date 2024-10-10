# car_service_management/urls.py

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

urlpatterns = [
    path('', lambda request: HttpResponseRedirect('/admin_panel/login/')),  # Перенаправление с пустого пути на страницу логина
    path('admin_panel/', include('admin_panel.urls')),  # Подключаем наше приложение
    path('admin/', admin.site.urls),
]
