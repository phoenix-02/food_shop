from django.urls import path
from shop import views

urlpatterns = [
    path('add/', views.add_dish, name="add"),
    path('', views.view_dishes, name="index"),
    path('login/', views.log_in, name="login"),
    path('register/', views.register, name="register"),
]
