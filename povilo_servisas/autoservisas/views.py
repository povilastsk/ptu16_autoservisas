from django.shortcuts import render, get_object_or_404
from . import models
from django.views import generic
from typing import Any



def index(request):
    context = {
        "num_cars": models.Car.objects.count(),
        "num_makes": models.CarModel.objects.values("make").distinct().count(),
        "num_orders": models.OrderLine.objects.count(),
        "parts_services": models.PartService.objects.all(),
    }
    return render(request, "library/index.html", context)

def parts_and_services(request):
    parts_and_services_list = models.PartService.objects.all().order_by("name")
    return render(
        request, 
        'parts_and_services.html', 
        {'partsandervices': parts_and_services_list}
    )

def brands(request):
    unique_brands = models.CarModel.objects.values("make").distinct()
    return render(
        request,
        "library/brand_list.html",
        {"brand_list": unique_brands},
    )

def brand_detail(request, brand):
    car_models = models.CarModel.objects.filter(make=brand)
    return render(
        request,
        "library/brand_detail.html",
        {"brand": brand, "car_models": car_models},
    )

def cars(request):
    return render(
        request,
        "library/car_list.html",
        {"car_list": models.Car.objects.all()}
        )

def orders(request):
    return render(
        request,
        "library/order_list.html",
        {"order_list": models.OrderLine.objects.all()}
        )