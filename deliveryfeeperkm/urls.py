from deliveryfeeperkm.views import *
from django.urls import path

app_name = 'deliveryfeeperkm'

urlpatterns = [
    path('', show_deliveryfee, name='show_deliveryfee'),
    path('create/', show_createdeliveryfee, name='show_createdeliveryfee'),
    path('update/<str:id>', update_deliveryfee, name='update_deliveryfee'),
    path('delete/<str:id>', delete_deliveryfee, name='delete_deliveryfee'),
    path('createdelivery/', create_deliveryfee, name='create_deliveryfee'),

]