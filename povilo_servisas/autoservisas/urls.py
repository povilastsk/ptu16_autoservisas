from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("brands/", views.brands, name="brands"),
    path("cars/", views.cars, name="cars"),
    path("orders/", views.orders, name="orders"),
]