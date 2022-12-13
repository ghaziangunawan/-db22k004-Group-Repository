from Ingredients.views import *
from django.urls import path


app_name = 'Ingredients'

urlpatterns = [
    path('', ingredient_read, name='ingredient_read'),
    path('create/', ingredient_create, name='ingredient_create'),
    path('delete/<int:ingredient_id>', delete_ingredient, name='delete_ingredient'),
]