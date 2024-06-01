from django import forms

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1)
    product_id = forms.IntegerField(widget=forms.HiddenInput)

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=120)
    