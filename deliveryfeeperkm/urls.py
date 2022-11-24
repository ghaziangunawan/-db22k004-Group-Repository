from deliveryfeeperkm.views import *
from django.urls import path

app_name = 'deliveryfeeperkm'

urlpatterns = [
    path('', show_deliveryfee, name='show_deliveryfee'),
    path('create/', show_createdeliveryfee, name='show_createdeliveryfee'),
    path('update/', show_updatedeliveryfee, name='show_updatedeliveryfee'),
]