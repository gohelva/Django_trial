from django.http import HttpResponse
from django.shortcuts import render

def home_view(request,*args, **kwarqs):
	#return HttpResponse("<h1>hello world</h1>")
	return render(request,"home.html",{})


def contact_view(request,*args, **kwarqs):
	#return HttpResponse("<h1>contact world</h1>")
	return render(request,"contact.html",{})

def about_view(request,*args, **kwarqs):
	#return HttpResponse("<h1>about world</h1>")
	my_context={
	"my_text":"this is about me",
	"my_number":124,
	"my_list":[124,24,12]

	}
	return render(request,"about.html",my_context)

def social_view(request,*args, **kwarqs):
	return HttpResponse("<h1> world</h1>")