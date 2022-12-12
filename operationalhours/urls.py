from operationalhours.views import show_operationalhours,show_operationalhourstime,show_edit,set_remove
from django.urls import path

app_name = 'operationalhours'

urlpatterns = [
    path('create', show_operationalhours, name='show_operationalhours'),
    path('', show_operationalhourstime, name='show_operationalhourstime'),
    path('edit/<initday>', show_edit, name='show_edit'),
    path("set_remove/<day>", set_remove, name="set_remove"),

]
