from django.urls import path
from .views import (
                        product_detail_view, 
                        product_create_view, 
                        dynamic_lookup_view
                     )

urlpatterns = [
	  path('<int:id>/',dynamic_lookup_view,name='product'),
	  path('detail/',product_detail_view,name='detail'),
	  path('',product_create_view,name='create')
]