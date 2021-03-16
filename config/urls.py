from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.rest_shop.urls')),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('', include('shop.urls')),
    path('', include('social_django.urls', namespace='social')),
    path('favicon.ico', RedirectView.as_view(url='/static/img/favicon.ico')),
    # media connecting
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
    staticfiles_urlpatterns()

# debug toolbar
if settings.DEBUG:
    # by default type is text-plain, thus browser reject working with
    import mimetypes
    mimetypes.add_type("application/javascript", ".js", True)

    import debug_toolbar
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))

# end debug toolbar
