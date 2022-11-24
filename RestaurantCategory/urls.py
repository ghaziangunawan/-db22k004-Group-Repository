from RestaurantCategory.views import *
from django.urls import path

app_name = 'RestaurantCategory'

urlpatterns = [
    path('', rest_category_read, name='rest_category_read'),
    path('create/', rest_category_create, name='rest_category_create'),
]