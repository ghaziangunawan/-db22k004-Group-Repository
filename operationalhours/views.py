from django.shortcuts import render
from django.shortcuts import render, redirect
from django.db import connection
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def show_operationalhours(request):   
    email = request.session.get('useremail')
    cursor = connection.cursor()
    search_path = 'set search_path to sirest'
    cursor.execute(search_path)
    if request.method == 'POST':
        response = HttpResponseRedirect(reverse('operationalhours:show_operationalhourstime'))
        day = request.POST.get('day')
        ophours = request.POST.get('ophour')
        closehours = request.POST.get('closehour')
        if not day or not ophours or not closehours:
            return render(request, 'operationalhours.html')
        
        else:
            SQL = f"""
        select rname
        from restaurant
        where email = '{email}'
        """
            cursor.execute(SQL)
            Rname = cursor.fetchall()[0][0]
            SQL = f"""
        select rbranch
        from restaurant
        where email = '{email}'
        """
            cursor.execute(SQL)
            Rbranch = cursor.fetchall()[0][0]
            SQL = f"""
            INSERT INTO restaurant_operating_hours VALUES ('{Rname}', '{Rbranch}',
            '{day}','{ophours}','{closehours}')
            """
            cursor.execute(SQL)
            return response
    return render(request, 'operationalhours.html')

@csrf_exempt
def show_operationalhourstime(request): 
    email = request.session.get('useremail')
    cursor = connection.cursor()
    search_path = 'set search_path to sirest'
    cursor.execute(search_path)
    SQL = f"""
        select rname
        from restaurant
        where email = '{email}'
        """
    cursor.execute(SQL)
    Rname = cursor.fetchall()[0][0]
    SQL = f"""
        select rbranch
        from restaurant
        where email = '{email}'
        """
    cursor.execute(SQL)
    Rbranch = cursor.fetchall()[0][0]

    SQL = f"""
        select day,starthours,endhours
        from restaurant_operating_hours
        where name='{Rname}' and branch='{Rbranch}'
        """
    cursor.execute(SQL)
    fetchOptime = cursor.fetchall()  
    print(fetchOptime)
    response = {'optime': fetchOptime}
    return render(request, 'operationalhourslist.html',response)

@csrf_exempt
def show_edit(request,initday): 
    email = request.session.get('useremail')  
    if request.method =='POST':
        response = HttpResponseRedirect(reverse('operationalhours:show_operationalhourstime'))
        cursor = connection.cursor()
        search_path = 'set search_path to sirest'
        cursor.execute(search_path)
        day = request.POST.get('day')
        ophours = request.POST.get('ophour')
        closehours = request.POST.get('closehour')
        if not day or not ophours or not closehours:
            return render(request, 'edit.html')
        SQL = f"""
        select rname
        from restaurant
        where email = '{email}'
        """
        cursor.execute(SQL)
        Rname = cursor.fetchall()[0][0]
        SQL = f"""
        select rbranch
        from restaurant
        where email = '{email}'
        """
        cursor.execute(SQL)
        Rbranch = cursor.fetchall()[0][0]
        SQL = f"""
        UPDATE restaurant_operating_hours
        SET day='{day}', starthours='{ophours}', endhours='{closehours}'
        where name='{Rname}' and branch='{Rbranch}' and day='{initday}'
        """
        cursor.execute(SQL)
        return response
    context = {'initday':initday}
    return render(request, 'edit.html',context)

@csrf_exempt
def set_remove(request,day):
    email = request.session.get('useremail')  
    response = HttpResponseRedirect(reverse('operationalhours:show_operationalhourstime'))
    cursor = connection.cursor()
    search_path = 'set search_path to sirest'
    cursor.execute(search_path)
    day = day
    SQL = f"""
        select rname
        from restaurant
        where email = '{email}'
        """
    cursor.execute(SQL)
    Rname = cursor.fetchall()[0][0]
    SQL = f"""
        select rbranch
        from restaurant
        where email = '{email}'
        """
    cursor.execute(SQL)
    Rbranch = cursor.fetchall()[0][0]
    SQL = f"""
        DELETE FROM restaurant_operating_hours 
        where name='{Rname}' and branch='{Rbranch}' and day='{day}'
        """
    cursor.execute(SQL)
    return response


