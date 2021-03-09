from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    # вставляем пути из приложения shop в основной список путей
    path('', include('shop.urls')),
    path('', include('social_django.urls', namespace='social')),
    path('favicon.ico', RedirectView.as_view(url='/static/img/favicon.ico')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
