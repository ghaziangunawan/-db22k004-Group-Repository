from user.views import *
from django.urls import path

app_name = 'user'

urlpatterns = [
    path('', show_register, name='show_register'),
    path('admin/', show_adminform, name='show_adminform'),
    path('customer/', show_customerform, name='show_customerform'),
    path('restaurant/', show_restaurantform, name='show_restarantform'),
    path('courier/', show_courierform, name='show_courierform'),
    path('dashboard/', show_userdashboard, name='show_userdashboard'),
    path('dashboardtable/', show_userdashboardtable, name='show_userdashboardtable'),
    path('profile/', show_userprofile, name='show_userprofile'),
]