from transactioncustomer.views import *
from django.urls import path

app_name = 'Food'

urlpatterns = [
    path('', show_inputfooddeliveryaddress, name='show_inputfooddeliveryaddress'),
    path('promo/', show_restaurantselection, name='show_restaurantselection'),
    path('selection/', show_pageselection, name='show_pageselection'),
    path('orderlist/', show_orderlist, name='show_orderlist'),
    path('confirmation/', show_paymentconfirmation, name='show_paymentconfirmation'),
    path('summary/', show_ordersummary, name='show_ordersummary'),
    path('ongoing/', show_ongoingorders, name='show_ongoingorders'),
    path('details/', show_orderdetails, name='show_orderdetails'),
]