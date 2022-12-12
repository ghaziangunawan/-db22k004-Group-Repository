from transaction.views import show_transaction,show_details, set_status
from django.urls import path

app_name = 'transaction'

urlpatterns = [
    path('', show_transaction, name='show_transaction'),
    path('details/<email>', show_details, name='show_details'),
    path("set_status/<email>/<datetime>/<status>", set_status, name="set_status"),
]
