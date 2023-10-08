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