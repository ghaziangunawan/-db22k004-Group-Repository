from TransactionCourier.views import *
from django.urls import path

app_name = 'TransactionCourier'

urlpatterns = [
    path('', transaction_courier, name='transaction_courier'),
    path('TransactionCourier/complete/<str:hash>', update_transaction_courier, name='update_transaction_courier'),
]