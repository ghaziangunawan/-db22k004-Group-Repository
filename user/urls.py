from user.views import *
from django.urls import path

app_name = 'user'

urlpatterns = [
    path('', show_register, name='show_register'),
    path('admin/', show_adminform, name='show_adminform'),
    path('customer/', show_customerform, name='show_customerform'),
    path('restaurant/', show_restaurantform, name='show_restaurantform'),
    path('courier/', show_courierform, name='show_courierform'),
    path('customerdashboard/', show_customerdashboard, name='show_customerdashboard'),
    path('admindashboard/', show_admindashboard, name='show_admindashboard'),
    path('restaurantdashboard/', show_restaurantdashboard, name='show_restaurantdashboard'),
    path('courierdashboard/', show_courierdashboard, name='show_courierdashboard'),
    path('profile/<role>/<email>', show_userprofile, name='show_userprofile'),
    path('verification/<email>', verification, name='verification'),
]