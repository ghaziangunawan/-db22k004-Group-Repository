from RestaurantCategory.views import *
from django.urls import path

app_name = 'RestaurantCategory'

urlpatterns = [
    path('', rest_category_read, name='rest_category_read'),
    path('create/', rest_category_create, name='rest_category_create'),
    path('delete/<int:rest_cat_id>', delete_rest_cat, name='delete_rest_cat'),
]