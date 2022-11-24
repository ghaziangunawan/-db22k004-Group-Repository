from django.shortcuts import render

# Create your views here.


def show_deliveryfee(request):   
    return render(request, 'deliveryfeeperkm.html')

def show_createdeliveryfee(request):   
    return render(request, 'createdeliveryfeeperkm.html')

def show_updatedeliveryfee(request):
    return render(request, 'updatedeliveryfeeperkm.html')