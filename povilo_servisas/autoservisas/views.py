from django.shortcuts import render
from . import models



def index(request):
    brands = models.CarModel.objects.values_list("make", flat=True).distinct()
    context = {
        "num_cars": models.Car.objects.count(),
        "num_makes": models.CarModel.objects.values("make").distinct().count(),
        "num_orders": models.OrderLine.objects.count(),
        "brands": brands,
    }
    return render(request, "library/index.html", context)