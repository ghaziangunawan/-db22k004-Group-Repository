from django.shortcuts import render
from django.shortcuts import render, redirect
from django.db import connection
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def show_operationalhours(request):   
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
            INSERT INTO restaurant_operating_hours VALUES ('Vidoo', 'Paget',
            '{day}','{ophours}','{closehours}')
            """
            cursor.execute(SQL)
            return response
    return render(request, 'operationalhours.html')

def show_operationalhourstime(request): 
    cursor = connection.cursor()
    search_path = 'set search_path to sirest'
    cursor.execute(search_path)
    SQL = f"""
        select day,starthours,endhours
        from restaurant_operating_hours
        where name='Vidoo' and branch='Paget'
        """
    cursor.execute(SQL)
    fetchOptime = cursor.fetchall()  
    print(fetchOptime)
    response = {'optime': fetchOptime}
    return render(request, 'operationalhourslist.html',response)

def show_edit(request,initday):   
    if request.method =='POST':
        response = HttpResponseRedirect(reverse('operationalhours:show_operationalhourstime'))
        cursor = connection.cursor()
        search_path = 'set search_path to sirest'
        cursor.execute(search_path)
        day = request.POST.get('day')
        ophours = request.POST.get('ophour')
        closehours = request.POST.get('closehour')
        SQL = f"""
        UPDATE restaurant_operating_hours
        SET day='{day}', starthours='{ophours}', endhours='{closehours}'
        where name='Vidoo' and branch='Paget' and day='{initday}'
        """
        cursor.execute(SQL)
        return response
    context = {'initday':initday}
    return render(request, 'edit.html',context)

def set_remove(request,day):
    response = HttpResponseRedirect(reverse('operationalhours:show_operationalhourstime'))
    cursor = connection.cursor()
    search_path = 'set search_path to sirest'
    cursor.execute(search_path)
    day = day
    SQL = f"""
        DELETE FROM restaurant_operating_hours 
        where name='Vidoo' and branch='Paget' and day='{day}'
        """
    cursor.execute(SQL)
    return response


