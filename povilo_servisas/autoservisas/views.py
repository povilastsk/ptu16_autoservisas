from django.shortcuts import render
from . import models

all_brands = models.CarModel.objects.values_list("make", flat=True)
unique_brands = set(all_brands)

def index(request):
    context = {
        "num_cars": models.Car.objects.count(),
        "num_makes": models.CarModel.objects.values("make").distinct().count(),
        "num_orders": models.OrderLine.objects.count(),
        "brands": unique_brands,
    }
    return render(request, "library/index.html", context)