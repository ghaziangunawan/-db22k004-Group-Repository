from django.shortcuts import render

# Create your views here.

def show_transaction(request):   
    return render(request, 'transaction.html')

def show_details(request):   
    return render(request, 'details.html')


