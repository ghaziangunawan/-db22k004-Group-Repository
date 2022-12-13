from Food.views import *
from django.urls import path

app_name = 'Food'

urlpatterns = [
    path('', show_foodlist, name='show_foodlist'),
    path('add/', show_addfood, name='show_addfood'),
    path('edit/', show_editfood, name='show_editfood'),
    path('restaurant/', show_restaurantlist, name='show_restaurantlist'),
    path('restaurantdetail/', show_restaurantmenu, name='show_restaurantmenu'),
]