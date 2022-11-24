from TransactionCourier.views import *
from django.urls import path

app_name = 'TransactionCourier'

urlpatterns = [
    path('', transaction_courier, name='transaction_courier'),
]