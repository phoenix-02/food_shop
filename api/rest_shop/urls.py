from django.urls import include, path
from rest_framework import routers
from api.rest_shop import views

router = routers.DefaultRouter()
router.register(r'companies', views.CompanyViewSet)
router.register(r'carts', views.CartViewSet)
router.register(r'dishes', views.DishViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('all-users/<int:pk>', views.UserViewSet.as_view()),
    path("all-profiles/", views.UserProfileListCreateView.as_view(), name="all-profiles"),
    path("profile/<int:pk>", views.UserProfileDetailView.as_view(), name="profile"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]