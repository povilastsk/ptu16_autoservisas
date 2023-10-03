from django.shortcuts import render, get_object_or_404
from . import models
from django.views import generic
from typing import Any



def index(request):
    brands = models.CarModel.objects.values_list("make", flat=True).distinct()
    context = {
        "num_cars": models.Car.objects.count(),
        "num_makes": models.CarModel.objects.values("make").distinct().count(),
        "num_orders": models.OrderLine.objects.count(),
        "brands": brands,
    }
    return render(request, "library/index.html", context)


def brands(request):
    brands = models.CarModel.objects.all()
    unique_brands = sorted(set(model.make for model in brands))
    return render(request, "library/brand_list.html", {"brand_list": unique_brands})

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