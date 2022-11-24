from transaction.views import show_transaction,show_details
from django.urls import path

app_name = 'transaction'

urlpatterns = [
    path('', show_transaction, name='show_transaction'),
    path('details/', show_details, name='show_details'),
]
