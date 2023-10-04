from django import forms

class BrandSearchForm(forms.Form):
    search_query = forms.CharField(label='Search', required=False)