from django.contrib import admin
from . import models
from . import models
from .forms import PartServiceReviewForm


class CarModelAdmin(admin.ModelAdmin):
    list_display = ("make", "model", "year")
    search_fields = ("make", "model", "year")
    list_filter = ("make", )


class CarAdmin(admin.ModelAdmin):
    list_display = ("owner", "car_model", "plate", "vin", "color")
    list_filter = ("car_model__make", "color")
    search_fields = ("owner__username", "car_model__make", "car_model__model", "plate", "vin", "owner__last_name")

class ServiceOrderAdmin(admin.ModelAdmin):
    list_display = ("date", "car", "status")
    list_filter = ("status", )
    search_fields = ("car__owner__username", "date", "status")
    date_hierarchy = "date"

class OrderLineAdmin(admin.ModelAdmin):
    list_display = ("order", "part_service", "quantity", "price")
    list_filter = ("order__car__owner__username", "part_service__name")
    search_fields = ("order__car__owner__username", "part_service__name")
    raw_id_fields = ("order", "part_service")


class PartServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "price")


class PartServiceReviewAdmin(admin.ModelAdmin):
    form = PartServiceReviewForm
    list_display = ("partservice", "reviewer", "created_at")
    list_display_links = ("created_at", )


admin.site.register(models.CarModel, CarModelAdmin)
admin.site.register(models.Car, CarAdmin)
admin.site.register(models.ServiceOrder, ServiceOrderAdmin)
admin.site.register(models.OrderLine, OrderLineAdmin)
admin.site.register(models.PartService, PartServiceAdmin)
admin.site.register(models.PartServiceReview, PartServiceReviewAdmin)