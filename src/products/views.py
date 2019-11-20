from django.shortcuts import render, get_object_or_404
from .models import Products
from .form import ProductForm, RawProductForm
# Create your views here.
def product_create_view(request):
	form = RawProductForm(request.POST)
	if form.is_valid():
		form.svae()
		form = ProductForm
	context ={
		"form": form
	}
	return render(request,"products/product_create.html",context)



def product_detail_view(request):
	obj = get_object_or_404(Products, id=id)
	context ={
	'object':obj
	}
	return render(request,"products/detail.html",context)


def dynamic_lookup_view(request,id):
	obj= get_object_or_404(Products,  id=id)
	context ={
		"object":obj
	}
	return render(request,"products/product_detial.html",context)