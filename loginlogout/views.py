from django.shortcuts import render, redirect
from django.db import connection
from django.http import HttpResponseRedirect
from django.urls import reverse

ssp = 'set search_path to sirest'
pss = 'set search_path to public'

# Create your views here.
def show_sirest(request):   
    return render(request, 'sirest.html')

def show_login(request):
    if request.method == "POST":
        cursor = connection.cursor()
        cursor.execute(ssp)   
        
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(email, password)

        sql = f"""
        SELECT *
        FROM USER_ACC
        WHERE Email = '{email}' AND Password = '{password}'
        """

        cursor.execute(sql)
        foundUser = cursor.fetchall()
        print(foundUser)

        if foundUser:
            sql = f"""
            SELECT * FROM ADMIN WHERE Email = '{email}'
            """
            cursor.execute(sql)
            isAdmin = bool(cursor.fetchone())

            sql = f"""
            SELECT * FROM COURIER WHERE Email = '{email}'
            """
            cursor.execute(sql)
            isCourier = bool(cursor.fetchone())

            sql = f"""
            SELECT * FROM CUSTOMER WHERE Email = '{email}'
            """
            cursor.execute(sql)
            isCustomer = bool(cursor.fetchone())

            sql = f"""
            SELECT * FROM RESTAURANT WHERE Email = '{email}'
            """
            cursor.execute(sql)
            isRestaurant = bool(cursor.fetchone())

            cursor.execute(pss)
            request.session['useremail'] = email
            request.session['isLoggedIn'] = True
            request.session['isAdmin'] = isAdmin
            request.session['isCourier'] = isCourier
            request.session['isCustomer'] = isCustomer
            request.session['isRestaurant'] = isRestaurant

            if(isAdmin): return redirect('user:show_admindashboard')
            if(isCourier): return redirect('user:show_courierdashboard')
            if(isCustomer): return redirect('user:show_customerdashboard')
            if(isRestaurant): return redirect('user:show_restaurantdashboard')

    return render(request, 'login.html')

def logout(request):
    request.session.flush()
    return redirect('loginlogout:show_sirest')
