from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.db.models.query import QuerySet, Q
from . import models
from .forms import BrandSearchForm
from django.views import generic
from typing import Any

class UserCarListView(LoginRequiredMixin, generic.ListView):
    model = models.Car
    template_name = "library/user_car_list.html"
    paginate_by = 5

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset
    

def index(request:HttpRequest):
    num_visits = request.session.get("num_visits", 1)
    request.session["num_visits"] = num_visits +1
    context = {
        "num_cars": models.Car.objects.count(),
        "num_makes": models.CarModel.objects.values("make").distinct().count(),
        "num_orders": models.OrderLine.objects.count(),
        "parts_services": models.PartService.objects.all(),
        "num_visits": num_visits,
    }
    return render(request, "library/index.html", context)

def parts_and_services(request:HttpRequest):
    parts_and_services_list = models.PartService.objects.all().order_by("name")
    return render(
        request, 
        'parts_and_services.html', 
        {'partsandervices': parts_and_services_list}
    )

def brands(request:HttpRequest):
    search_query = request.GET.get("search_query")
    if request.GET.get("reset_search"):
        return redirect("brands")
    if search_query:
        car_models = models.CarModel.objects.filter(make__icontains=search_query)
    else:
        car_models = models.CarModel.objects.all()
    unique_brands = sorted(set(model.make for model in car_models))
    page_number = request.GET.get("page")
    items_per_page = 3
    paginator = Paginator(unique_brands, items_per_page)
    page_obj = paginator.get_page(page_number)

    search_form = BrandSearchForm(initial={"search_query": search_query})

    return render(
        request,
        "library/brand_list.html",
        {"brand_list": page_obj, "search_form": search_form},
    )

def brand_detail(request:HttpRequest, brand):
    car_models = models.CarModel.objects.filter(make=brand)
    return render(
        request,
        "library/brand_detail.html",
        {"brand": brand, "car_models": car_models},
    )

def cars(request:HttpRequest):
    return render(
        request,
        "library/car_list.html",
        {"car_list": models.Car.objects.all()}
        )

def orders(request:HttpRequest):
    return render(
        request,
        "library/order_list.html",
        {"order_list": models.OrderLine.objects.all()}
        )