from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('(<category_slug>[-\w]+)/', views.product_list, name='product_list_by_category'),
    path('(<id>\d+)/(<slug>[-\w]+)/', views.product_detail, name='product_detail'),
]