from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('brands/', views.brands, name='brands'),
    path('brands/<str:brand>/', views.brand_detail, name='brand_detail'),
    path('car/<int:car_id>/service-orders/', views.CarServiceOrderListView.as_view(), name='car_service_orders'),
    path('cars/my/', views.UserCarListView.as_view(), name="user_cars"),
    path('parts-and-services/', views.PartServiceListView.as_view(), name='parts_and_services'),
]