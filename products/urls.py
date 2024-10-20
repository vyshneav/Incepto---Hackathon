from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('list_product/',views.showproducts,name='list_product'),
    # path('product_detail/',views.detail_product,name='product_detail')

    
]