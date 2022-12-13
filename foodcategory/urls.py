from foodcategory.views import *
from django.urls import path

app_name = 'foodcategory'

urlpatterns = [
    path('', show_food_category, name='show_food_category'),
    path('create/', add_food_category, name='add_food_category'),
    path('delete/<name>', delete_food_category, name='delete_food_category')
]