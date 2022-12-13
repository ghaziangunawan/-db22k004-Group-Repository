from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import connection
from django.core.exceptions import PermissionDenied

ssp = 'set search_path to sirest'

# Create your views here.
def transaction_courier(request):
    if not request.session.get('isLoggedIn'): return redirect('loginlogout:show_login')
    if not request.session.get('isCourier'): raise PermissionDenied()

    cr_email = request.session.get('useremail')

    cursor = connection.cursor()
    cursor.execute(ssp)

    sql = f"""
    ALTER TABLE TRANSACTION
    ADD Hash VARCHAR(50)
    """

    try:
        cursor.execute(sql)
    except Exception:
        pass

    sql = f"""
    SELECT T.Email, T.Datetime
    FROM TRANSACTION T
    LEFT JOIN TRANSACTION_HISTORY TH 
    ON T.EMail = TH.Email AND T.Datetime = TH.Datetime
    WHERE CourierId = '{cr_email}'
    GROUP BY (T.Email, T.Datetime)
    HAVING MAX(TSId) <= '3'
    """

    cursor.execute(sql)
    datas = cursor.fetchall()

    data = []
    for (email, datetime) in datas:
        datatemp = [str(datetime)]
        # print(datatemp)

        sql = f"""
        SELECT CONCAT(FName, ' ', LName)
        FROM USER_ACC
        WHERE Email = '{email}'
        """

        cursor.execute(sql)
        temp = cursor.fetchall()
        # print(temp)
        datatemp.extend(list(temp[0]))
        
        sql = f"""
        SELECT Street, District, City, Province
        FROM TRANSACTION
        WHERE Email = '{email}' AND Datetime = '{datetime}'
        """

        cursor.execute(sql)
        temp = cursor.fetchall()
        # print(temp)
        datatemp.extend(list(temp[0]))

        sql = f"""
        SELECT CONCAT(R.RName, ' ', R.RBranch), Street, District, City, Province
        FROM RESTAURANT R, TRANSACTION_FOOD TF
        WHERE TF.Email = '{email}' AND TF.Datetime = '{datetime}' AND
            R.RName = TF.RName AND R.RBranch = TF.RBranch
        """

        cursor.execute(sql)
        temp = cursor.fetchone()
        # print(temp)
        datatemp.extend(list(temp))

        sql = f"""
        SELECT FoodName, Amount, Note
        FROM TRANSACTION_FOOD
        WHERE Email = '{email}' AND Datetime = '{datetime}'
        """

        cursor.execute(sql)
        temp = cursor.fetchall()
        # print(temp)
        datatemp.append(temp)

        sql = f"""
        SELECT TotalFood, TotalDiscount, DeliveryFee, TotalPrice, PM.Name, PS.Name
        FROM TRANSACTION, PAYMENT_METHOD PM, PAYMENT_STATUS PS
        WHERE Email = '{email}' AND Datetime = '{datetime}' AND
            PMId = PM.Id AND PSId = PS.Id
        """

        cursor.execute(sql)
        temp = cursor.fetchall()
        # print(temp)
        datatemp.extend(list(temp[0]))

        sql = f"""
        SELECT DISTINCT Name
        FROM TRANSACTION_HISTORY
        LEFT JOIN TRANSACTION_STATUS 
        ON TSId = Id
        WHERE Id = (
            SELECT MAX(TSId)
            FROM TRANSACTION_HISTORY
            WHERE Email = '{email}' AND Datetime = '{datetime}'
            GROUP BY Email, Datetime
            )
        """

        cursor.execute(sql)
        temp = cursor.fetchall()
        # print(temp)
        datatemp.extend(list(temp[0]))

        sql = f"""
        SELECT CONCAT(FName, ' ', LName)
        FROM USER_ACC
        WHERE Email = '{cr_email}'
        """

        cursor.execute(sql)
        temp = cursor.fetchall()
        # print(temp)
        datatemp.extend(list(temp[0]))

        sql = f"""
        SELECT PlateNum, VehicleType, VehicleBrand
        FROM COURIER
        WHERE Email = '{cr_email}'
        """

        cursor.execute(sql)
        temp = cursor.fetchall()
        # print(temp)
        datatemp.extend(list(temp[0]))

        datahash = hash(email + str(datetime))
        datatemp.append(str(datahash))

        sql = f"""
        UPDATE TRANSACTION
        SET Hash = '{datahash}'
        WHERE Email = '{email}' AND Datetime = '{datetime}'
        """

        cursor.execute(sql)
        
        data.append(datatemp)
        # print(data)
    
    context = {
        'datas': data,
    }

    return render(request, 'transaction_courier.html', context)

def update_transaction_courier(request, hash):
    if not request.session.get('isLoggedIn'): return redirect('loginlogout:show_login')
    if not request.session.get('isCourier'): raise PermissionDenied()

    cr_email = request.session.get('useremail')

    cursor = connection.cursor()
    cursor.execute(ssp)

    sql = f"""
    SELECT Email, Datetime, CourierId
    FROM TRANSACTION
    WHERE Hash = '{hash}'
    """

    cursor.execute(sql)
    (email, datetime, courierid) = cursor.fetchone()
    # print(email, datetime)

    if courierid != cr_email: raise PermissionDenied()

    sql = f"""
    INSERT INTO TRANSACTION_HISTORY VALUES
    ('{email}', '{datetime}', '4', '{datetime.now()}')
    """

    cursor.execute(sql)

    return HttpResponseRedirect(reverse('TransactionCourier:transaction_courier'))