from django.shortcuts import render, redirect
from django.db import connection
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def show_restopay(request):
    # Start Copy Here For Login Required Function
    cursor = connection.cursor()
    cursor.execute("SET search_path to PUBLIC")

    if not request.session.get("isLoggedIn"):
        print(request.session.get("useremail"))
        return redirect('loginlogout:show_login')

    cursor = connection.cursor()
    search_path = 'set search_path to sirest'
    cursor.execute(search_path)
    SQL = f"""
    SELECT restopay
    FROM transaction_actor
    WHERE email = '{request.session.get("useremail")}'
    """
    cursor.execute(SQL)
    fetchBalance = cursor.fetchall()  
    response = {'balance': str(fetchBalance[0][0])}
    return render(request, 'restopay.html',response)

def show_withdraw(request):
    cursor = connection.cursor()
    search_path = 'set search_path to sirest'
    cursor.execute(search_path)
    SQL = f"""
    SELECT restopay
    FROM transaction_actor
    WHERE email = '{request.session.get("useremail")}'
    """
    cursor.execute(SQL)
    fetchBalance = cursor.fetchall()  
    response = {'balance': str(fetchBalance[0][0])}
    if request.method == 'POST':
        response = HttpResponseRedirect(reverse('restopay:show_restopay'))
        amount = request.POST.get('Amount')
        cursor = connection.cursor()
        search_path = 'set search_path to sirest'
        cursor.execute(search_path)
        SQL = f"""
        select withdraw('{request.session.get("useremail")}', {amount})
        """
        cursor.execute(SQL)
        return response
    return render(request, 'withdraw.html',response)

def show_topup(request):
    cursor = connection.cursor()
    search_path = 'set search_path to sirest'
    cursor.execute(search_path)
    SQL = f"""
    SELECT restopay
    FROM transaction_actor
    WHERE email = '{request.session.get("useremail")}'
    """
    cursor.execute(SQL)
    fetchBalance = cursor.fetchall()  
    response = {'balance': str(fetchBalance[0][0])}   
    if request.method == 'POST':
        response = HttpResponseRedirect(reverse('restopay:show_restopay'))
        amount = request.POST.get('Amount')
        cursor = connection.cursor()
        search_path = 'set search_path to sirest'
        cursor.execute(search_path)
        SQL = f"""
        UPDATE transaction_actor
        SET restopay = restopay + {amount}
        WHERE email = '{request.session.get("useremail")}'
        """
        cursor.execute(SQL)
        return response
    return render(request, 'topup.html',response)