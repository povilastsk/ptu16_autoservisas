from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('brands/', views.brands, name='brands'),
    path('cars/', views.cars, name='cars'),
    path('brands/<str:brand>/', views.brand_detail, name='brand_detail'),
    path('orders/', views.orders, name='orders'),
    path('cars/my/', views.UserCarListView.as_view(), name="user_cars")
]