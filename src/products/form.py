from django import forms
from .models import Products

class ProductForm(forms.ModelForm):
	class Meta:
		model = Products
		fields= [
		'title',
		'description',
		'price'
		]

class RawProductForm(forms.Form):
	title         = forms.CharField(max_length=120)
	description   = forms.CharField(required=False,max_length=120)
	price         = forms.DecimalField()


