from django.shortcuts import render
from django.shortcuts import render, redirect
from django.db import connection
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def show_transaction(request):
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
    cursor.execute(search_path)
    SQL = f"""
        select fname,lname, transaction.datetime, transaction_Status.name, transaction_history.email, transaction_history.datetime 
        from transaction join user_acc on transaction.email = user_acc.email join transaction_history on transaction.email = transaction_history.email join transaction_Status on TSid = transaction_status.id
        join transaction_food on transaction.email = transaction_food.email 
        where not (transaction_status.id = '3' OR transaction_status.id = '4' OR transaction_status.id = '5') AND rname = '{Rname}' and rbranch = '{Rbranch}'
        """
    cursor.execute(SQL)
    fetchTransaction = cursor.fetchall()  
    print(fetchTransaction)
    response = {'transactions': fetchTransaction}
    return render(request, 'transaction.html',response) 
    

def show_details(request,email):
    useremail = request.session.get('useremail')    
    cursor = connection.cursor()
    search_path = 'set search_path to sirest'
    cursor.execute(search_path)
    SQL = f"""
        select rname
        from restaurant
        where email = '{useremail}'
        """
    cursor.execute(SQL)
    Rname = cursor.fetchall()[0][0]
    SQL = f"""
        select rbranch
        from restaurant
        where email = '{useremail}'
        """
    cursor.execute(SQL)
    Rbranch = cursor.fetchall()[0][0]
    SQL = f"""
    select *
    from transaction join transaction_food on transaction.email = transaction_food.email and transaction.datetime = transaction_food.datetime
    join user_acc on user_acc.email = transaction.email join restaurant on restaurant.rname = transaction_food.rname and restaurant.rbranch = transaction_food.rbranch
    join payment_method on PMid = payment_method.id join payment_status on PSid = payment_status.id join transaction_history on transaction.email = transaction_history.email and transaction.datetime = transaction_history.datetime
    join transaction_status on TSid = transaction_status.id join courier on CourierId = Courier.email
    where restaurant.rname = '{Rname}' and restaurant.rbranch = '{Rbranch}' and transaction.email = '{email}'
    """
    cursor.execute(SQL)
    fetchDetail = cursor.fetchall()
    print(fetchDetail)
    foodList = []
    for i in fetchDetail:
        foodList.append([i[20],i[22]])
    print(foodList)

    response = {'datetime':fetchDetail[0][1], 'custName':str(fetchDetail[0][26]) + " "+ str( fetchDetail[0][27]), 'CStreet': fetchDetail[0][2],
    'Cdistrict':fetchDetail[0][3],'CCity':fetchDetail[0][4], 'CProvince':fetchDetail[0][5], 'Rname':fetchDetail[0][18],'RBranch':fetchDetail[0][19],
    'RStreet': fetchDetail[0][32],'RDistrict' : fetchDetail[0][33], 'RCity':fetchDetail[0][33], 'RProvince':fetchDetail[0][34], 'foods':foodList, 'foodPrice':fetchDetail[0][6],
    'totaldiscount':fetchDetail[0][7], 'deliveryfee':fetchDetail[0][8],'totalprice':fetchDetail[0][9],'payment_methode':fetchDetail[0][-15],'payment_status':fetchDetail[0][-13],
    'transaction_status':fetchDetail[0][-6],'courier':fetchDetail[0][-5],'plateno':fetchDetail[0][-4],'vehicletype':fetchDetail[0][-2],'vehiclebrand':fetchDetail[0][-1] }
    return render(request, 'details.html',response)

def set_status(request,email,datetime,status):
    cursor = connection.cursor()
    search_path = 'set search_path to sirest'
    cursor.execute(search_path)
    if status == 'Waiting for restaurant':
        SQL = f"""
         UPDATE TRANSACTION_HISTORY
         SET tsid = '2' , datetimestatus =  CURRENT_TIMESTAMP
         WHERE email = '{email}' AND datetime = '{datetime}' 
        """
        cursor.execute(SQL)
    elif status == 'Order Made':
        SQL = f"""
         UPDATE TRANSACTION_HISTORY
         SET tsid = '3' , datetimestatus =  CURRENT_TIMESTAMP
         WHERE email = '{email}' AND datetime = '{datetime}' 
        """
        cursor.execute(SQL)
        SQL2 = f"""
        SELECT email, vehicletype
        FROM courier
        ORDER BY random()
        LIMIT 1
        """
        cursor.execute(SQL2)
        fetchCourier = cursor.fetchall()
        courierEmail = fetchCourier[0][0]
        courierVehicleType = fetchCourier[0][1]
        
        SQL3 = f"""
        UPDATE TRANSACTION
        SET CourierID = '{courierEmail}', vehicletype = '{courierVehicleType}'
        WHERE Email = '{email}'
        """
        cursor.execute(SQL3)
    return HttpResponseRedirect(reverse('transaction:show_transaction'))




