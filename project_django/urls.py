"""project_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('example_app.urls')),
    path('RestoPay/', include('RestoPay.urls')),
    path('operationalhours/', include('operationalhours.urls')),
    path('transaction/', include('transaction.urls')),
    path('deliveryfeeperkm/', include('deliveryfeeperkm.urls')),
    path('Food/', include('Food.urls')),
    path('RestaurantCategory/', include('RestaurantCategory.urls')),
    path('TransactionCourier/', include('TransactionCourier.urls')),
    path('Ingredients/', include('Ingredients.urls')),
    path('loginlogout/', include('loginlogout.urls')),
    path('user/', include('user.urls')),
    path('foodcategory/', include('foodcategory.urls')),
    path('transactioncustomer/', include('transactioncustomer.urls'))
]

# TODO: Implement Routings Here