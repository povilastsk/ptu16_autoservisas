from django.shortcuts import render
from . import models

def parts_and_services(request):
    parts_and_services_list = models.PartService.objects.all()
    return render(request, 'parts_and_services.html', {'partsandervices': parts_and_services_list})

def index(request):
    context = {
        "num_cars": models.Car.objects.count(),
        "num_makes": models.CarModel.objects.values('make').distinct().count(),
        "num_orders": models.OrderLine.objects.count(),
        "parts_services": models.PartService.objects.all(),
    }
    return render(request, "library/index.html", context)