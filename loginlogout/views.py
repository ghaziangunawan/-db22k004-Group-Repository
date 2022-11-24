from django.shortcuts import render

# Create your views here.

def show_sirest(request):   
    return render(request, 'sirest.html')

def show_login(request):   
    return render(request, 'login.html')