from django.shortcuts import render
from django.core.paginator import Paginator
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
    car_models = models.CarModel.objects.all()
    unique_brands = sorted(set(model.make for model in car_models))

    page_number = request.GET.get('page')
    items_per_page = 3

    paginator = Paginator(unique_brands, items_per_page)
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "library/brand_list.html",
        {"brand_list": page_obj},
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