from django.shortcuts import render, redirect
from django.db import connection
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def show_restopay(request):
    # Start Copy Here For Login Required Function
    email = request.session.get('useremail')
    cursor = connection.cursor()
    cursor.execute("SET search_path to PUBLIC")

    if not request.session.get("isLoggedIn"):
        return redirect('loginlogout:show_login')

    cursor = connection.cursor()
    search_path = 'set search_path to sirest'
    cursor.execute(search_path)
    SQL = f"""
    SELECT restopay
    FROM transaction_actor
    WHERE email = '{email}'
    """
    cursor.execute(SQL)
    fetchBalance = cursor.fetchall()  
    response = {'balance': str(fetchBalance[0][0])}
    return render(request, 'restopay.html',response)

def show_withdraw(request):
    email = request.session.get('useremail')
    cursor = connection.cursor()
    search_path = 'set search_path to sirest'
    cursor.execute(search_path)
    SQL = f"""
    SELECT restopay
    FROM transaction_actor
    WHERE email = '{email}'
    """
    cursor.execute(SQL)
    fetchBalance = cursor.fetchall()  
    context = {'balance': str(fetchBalance[0][0])}
    if request.method == 'POST':
        response = HttpResponseRedirect(reverse('restopay:show_restopay'))
        amount = request.POST.get('Amount')
        bank = request.POST.get('bankName')
        account = request.POST.get('AccountNumber')
        if not amount or not bank or not account:
            return render(request, 'withdraw.html',context)
        cursor = connection.cursor()
        search_path = 'set search_path to sirest'
        cursor.execute(search_path)
        SQL = f"""
        select withdraw('{email}', {amount})
        """
        cursor.execute(SQL)
        return response
    return render(request, 'withdraw.html',context)

def show_topup(request):
    email = request.session.get('useremail')
    cursor = connection.cursor()
    search_path = 'set search_path to sirest'
    cursor.execute(search_path)
    
    SQL = f"""
    SELECT restopay
    FROM transaction_actor
    WHERE email = '{email}'
    """
    cursor.execute(SQL)
    fetchBalance = cursor.fetchall()  
    context = {'balance': str(fetchBalance[0][0])}   
    if request.method == 'POST':
        response = HttpResponseRedirect(reverse('restopay:show_restopay'))
        amount = request.POST.get('Amount')
        bank = request.POST.get('BankName')
        account = request.POST.get('AccountNumber')
        if not amount or not bank or not account:
            return render(request, 'topup.html',context)
        cursor = connection.cursor()
        search_path = 'set search_path to sirest'
        cursor.execute(search_path)
        SQL = f"""
        UPDATE transaction_actor
        SET restopay = restopay + {amount}
        WHERE email = '{email}'
        """
        cursor.execute(SQL)
        return response
    return render(request, 'topup.html',context)