from django.urls import path
from . import views

urlpatterns = [
    path('my_cars/', views.UserCarListView.as_view(), name='my_cars'),
    path('', views.index, name='index'),
    path('brands/', views.brands, name='brands'),
    path('brands/<str:brand>/', views.brand_detail, name='brand_detail'),
    path('car/<int:car_id>/service-orders/', views.CarServiceOrderListView.as_view(), name='car_service_orders'),
    path('user_car_list/', views.UserCarListView.as_view(), name='user_car_list'),
    path('parts-and-services/', views.PartServiceListView.as_view(), name='parts_and_services'),
    path('parts-and-services/<int:pk>/', views.PartServiceDetailView.as_view(), name='partservice_detail'),
    path('review/create/', views.review_create, name='review_create'),
    path('place_order/<int:car_id>/', views.PlaceOrderView.as_view(), name='place_order'),
    path('cancel_order/<int:order_id>/', views.CancelOrderView.as_view(), name='cancel_order'),
    path('add_car/', views.add_car, name='add_car'),

]