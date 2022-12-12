from django.shortcuts import render
from django.shortcuts import render, redirect
from django.db import connection
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def show_sirest(request):   
    return render(request, 'sirest.html')

def show_login(request):
    cursor = connection.cursor()
    search_path = "SET search_path to SIREST"
    cursor.execute(search_path)   
    if request.method == "POST":
        email = request.POST.get('username')
        password = request.POST.get('password')
        

    return render(request, 'login.html')
    