from django.shortcuts import render

# Create your views here.

def show_restaurantselection(request):   
    return render(request, 'restaurantselection.html')

def show_inputfooddeliveryaddress(request):   
    return render(request, 'inputfooddeliveryaddress.html')

def show_pageselection(request):
    return render(request, 'pageselection.html')

def show_orderlist(request):   
    return render(request, 'orderlist.html')

def show_paymentconfirmation(request):
    return render(request, 'paymentconfirmation.html')

def show_ordersummary(request):
    return render(request, 'ordersummary.html')

def show_ongoingorders(request):
    return render(request, 'ongoingorders.html')

def show_orderdetails(request):
    return render(request, 'detailorder.html')