from Ingredients.views import ingredient_create
from Ingredients.views import ingredient_read
from django.urls import path


app_name = 'Ingredients'

urlpatterns = [
    path('create/', ingredient_create, name='ingredient_create'),
    path('', ingredient_read, name='ingredient_read'),
]