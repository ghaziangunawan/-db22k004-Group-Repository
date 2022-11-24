from foodcategory.views import *
from django.urls import path

app_name = 'foodcategory'

urlpatterns = [
    path('', show_foodcategorylist, name='show_foodcategorylist'),
    path('create/', show_createfoodcategory, name='show_createfoodcategory'),
]