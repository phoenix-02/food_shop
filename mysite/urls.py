from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # вставляем пути из приложения shop в основной список путей
    path('', include('shop.urls')),
    path('', include('shop.urls')),
]
