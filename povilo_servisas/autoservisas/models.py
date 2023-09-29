from django.db import models
from django.utils.translation import gettext_lazy as _ 
from django.urls import reverse
import uuid
# Create your models here.

class CarModel(models.Model):

    make = models.CharField(_("make"), max_length=100, db_index=True)
    model = models.CharField(_("model"), max_length=100, db_index=True)
    year = models.IntegerField(_("year"), db_index=True)

    class Meta:
        verbose_name = _("car model")
        verbose_name_plural = _("car models")
        ordering = ["make", "model", "year"]

    def __str__(self):
        return f"{self.make} - {self.model} - {self.year}"

    def get_absolute_url(self):
        return reverse("carmodel_detail", kwargs={"pk": self.pk})
    

class Car(models.Model):
    customer = models.CharField(_("customer"), max_length=100, db_index=True)
    car_model = models.ForeignKey(
        CarModel,
        verbose_name=_("car model"),
        on_delete=models.CASCADE,
        related_name="cars",
        )
    plate = models.CharField(_("plate"), max_length=50, null=True, blank=True, db_index=True)
    vin = models.CharField(_("vin"), max_length=17, null=True, blank=True, db_index=True)
    color = models.CharField(_("color"), max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = _("car")
        verbose_name_plural = _("cars")

    def __str__(self):
        return f"{self.customer}: {self.car_model} - Plate No.{self.plate}"

    def get_absolute_url(self):
        return reverse("car_detail", kwargs={"pk": self.pk})

SERVICEORDER_STATUS = (
    (0, _("pending")),
    (1, _("processing")),
    (2, _("completed")),
    (3, _("cancelled")),
)

class ServiceOrder(models.Model):
    car = models.ForeignKey(
        Car,
        verbose_name=_("car"), 
        on_delete=models.CASCADE
    )
    date = models.DateField(_("date"), auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = _("service order")
        verbose_name_plural = _("service orders")

    def __str__(self):
        return f"Date: {self.date} - {self.car}"

    def get_absolute_url(self):
        return reverse("serviceorder_detail", kwargs={"pk": self.pk})


class PartService(models.Model):
    name = models.CharField(_("name"), max_length=50, db_index=True)
    price = models.DecimalField(_("price"), max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("part or service")
        verbose_name_plural = _("parts and services")

    def __str__(self):
        return f" {self.name} {self.price}"

    def get_absolute_url(self):
        return reverse("partservice_detail", kwargs={"pk": self.pk})


class OrderLine(models.Model):
    order = models.ForeignKey(
        ServiceOrder, 
        verbose_name=_("order"), 
        on_delete=models.CASCADE,
        related_name="lines",
        db_index=True,
        null=False,
        )
    part_service = models.ForeignKey(
        PartService, 
        verbose_name=_("part service id"), 
        on_delete=models.CASCADE,
        related_name="lines",
        null=False,
        )
    quantity = models.IntegerField(_("quantity"), default=1)
    price = models.DecimalField(_("price"), max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("order line")
        verbose_name_plural = _("order lines")
        ordering = ["order"]

    def __str__(self):
        return f"{self.order} - {self.part_service} - {self.quantity} - {self.price}"

    def get_absolute_url(self):
        return reverse("orderline_detail", kwargs={"pk": self.pk})
