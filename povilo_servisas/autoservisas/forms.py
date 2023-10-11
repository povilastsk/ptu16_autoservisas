from django import forms
from . import models

class BrandSearchForm(forms.Form):
    search_query = forms.CharField(label='Search', required=False)


class PartServiceReviewForm(forms.ModelForm):
    class Meta:
        model = models.PartServiceReview
        fields = ('content', 'partservice')
        widgets = {
            'partservice': forms.HiddenInput(),
        }
        labels = {
            'content': '',
        }


class OrderForm(forms.Form):
    part_service = forms.ModelChoiceField(
        queryset=models.PartService.objects.all(),
        label="Select Part or Service",
    )
    quantity = forms.IntegerField(min_value=1, label="Quantity", initial=1)


class CarCreationForm(forms.ModelForm):
    make = forms.CharField(label="Make", max_length=100)
    model = forms.CharField(label="Model", max_length=100)
    year = forms.IntegerField(label="Year")

    class Meta:
        model = models.Car
        fields = ['make', 'model', 'year', 'plate', 'vin', 'color']