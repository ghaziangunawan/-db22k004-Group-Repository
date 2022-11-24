from django.shortcuts import render

# Create your views here.


def show_restopay(request):   
    return render(request, 'restopay.html')

def show_withdraw(request):   
    return render(request, 'withdraw.html')

def show_topup(request):   
    return render(request, 'topup.html')