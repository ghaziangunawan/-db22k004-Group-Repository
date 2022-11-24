from operationalhours.views import show_operationalhours,show_operationalhourstime,show_edit
from django.urls import path

app_name = 'operationalhours'

urlpatterns = [
    path('', show_operationalhours, name='show_operationalhours'),
    path('ophourslist/', show_operationalhourstime, name='show_operationalhourstime'),
    path('edit/', show_edit, name='show_edit'),

]
