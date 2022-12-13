from loginlogout.views import *
from django.urls import path

app_name = 'loginlogout'

urlpatterns = [
    path('', show_sirest, name='show_sirest'),
    path('login/', show_login, name='show_login'),
    path('logout/', logout, name='logout'),
]