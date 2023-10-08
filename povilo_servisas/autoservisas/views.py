from typing import Any
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse
from . import models, forms
from .forms import BrandSearchForm


class UserCarListView(LoginRequiredMixin, generic.ListView):
    model = models.Car
    template_name = "library/user_car_list.html"
    paginate_by = 5

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset
    

class CarServiceOrderListView(generic.ListView):
    model = models.ServiceOrder
    template_name = 'library/serviceorder_list.html'
    context_object_name = 'service_orders'

    def get_queryset(self):
        car = get_object_or_404(models.Car, pk=self.kwargs['car_id'])
        return models.ServiceOrder.objects.filter(car=car)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = get_object_or_404(models.Car, pk=self.kwargs['car_id'])
        context['car'] = car
        return context
    

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


def orders(request:HttpRequest):
    return render(
        request,
        "library/order_list.html",
        {"order_list": models.OrderLine.objects.all()}
        )


class PartServiceListView(generic.ListView):
    model = models.PartService
    template_name = 'library/partservice_list.html'
    context_object_name = 'partsandervices'

    def get_queryset(self):
        return models.PartService.objects.all().order_by('name')
    

class PartServiceDetailView(generic.edit.FormMixin, generic.DetailView):
    model = models.PartService
    template_name = 'library/partservice_detail.html'
    context_object_name = 'partservice'
    form_class = forms.PartServiceReviewForm

    def get_initial(self):
        initial = super().get_initial()
        initial['partservice'] = self.get_object()
        initial['reviewer'] = self.request.user
        return initial

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.partservice = self.object
        form.instance.reviewer = self.request.user
        form.save()
        messages.success(self.request, 'Review posted successfully.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('partservice_detail', kwargs={'pk': self.object.pk})
    
def review_create(request: HttpRequest):
    if request.method == 'POST':
        form = forms.PartServiceReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer = request.user
            review.save()
            messages.success(request, 'Review posted successfully.')
            return redirect('partservice_detail', pk=review.partservice.pk)
    else:
        form = forms.PartServiceReviewForm()

    return render(request, 'partservice_review_create.html', {'form': form})