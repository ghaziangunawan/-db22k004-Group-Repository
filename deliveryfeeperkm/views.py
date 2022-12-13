from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import connection
from django.core.exceptions import PermissionDenied
# from delivery_fee.models import Task
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def show_deliveryfee(request):
    if not request.session.get('isLoggedIn'): return redirect('loginlogout:show_login')
    if not request.session.get('isAdmin'): raise PermissionDenied()

    cursor = connection.cursor()
    cursor.execute("SET search_path to SIREST;")
    SQL = f"""
	SELECT * FROM DELIVERY_FEE_PER_KM
	"""
    cursor.execute(SQL)
    deliveryfee = cursor.fetchall()

    context = {'deliveryfee': deliveryfee}
    return render(request, 'deliveryfeeperkm.html', context)

@csrf_exempt
def create_deliveryfee(request):
    if not request.session.get('isLoggedIn'): return redirect('loginlogout:show_login')
    if not request.session.get('isAdmin'): raise PermissionDenied()

    cursor = connection.cursor()
    cursor.execute("SET search_path to SIREST")
    
    if request.method == "POST":
        province = request.POST.get('province')
        motorfee = request.POST.get('motorfee')
        carfee = request.POST.get('carfee')

        SQL = f"""
        SELECT MAX(CAST(Id AS NUMERIC)) FROM DELIVERY_FEE_PER_KM;
        """
        cursor.execute(SQL)
        checkid = cursor.fetchone()

        newid = 1
        if checkid[0]:
            newid = int(checkid[0]) + 1

        if province and motorfee and carfee:
            SQL = f"""
            INSERT INTO DELIVERY_FEE_PER_KM
            VALUES ('{newid}', '{province}', '{motorfee}', '{carfee}')
            """
            cursor.execute(SQL)
            return redirect('deliveryfeeperkm:show_deliveryfee')

    return render(request, "createdeliveryfeeperkm.html")

@csrf_exempt
def update_deliveryfee(request, id):
    if not request.session.get('isLoggedIn'): return redirect('loginlogout:show_login')
    if not request.session.get('isAdmin'): raise PermissionDenied()
   
    cursor = connection.cursor()
    cursor.execute("SET search_path to SIREST")

    if request.method == "POST":
        addmotorfee = request.POST.get('motorfee')
        addcarfee = request.POST.get('carfee')

        if addmotorfee and addcarfee:
            
            SQL = f"""
            UPDATE DELIVERY_FEE_PER_KM
            SET motorfee = '{addmotorfee}', carfee = '{addcarfee}'
            WHERE id = '{id}'; 
            """
            cursor.execute(SQL)

            return redirect('deliveryfeeperkm:show_deliveryfee')

    SQL = f"""
    SELECT province FROM DELIVERY_FEE_PER_KM WHERE id = '{id}'
    """

    cursor.execute(SQL)
    nameofprov = cursor.fetchone()
    context = {'deliveryfee': nameofprov}
    return render(request, "updatedeliveryfeeperkm.html", context)

        
@csrf_exempt
def delete_deliveryfee(request, id):
    if not request.session.get('isLoggedIn'): return redirect('loginlogout:show_login')
    if not request.session.get('isAdmin'): raise PermissionDenied()
    
    cursor = connection.cursor()

    cursor.execute("SET search_path to SIREST")

    SQL = f"""
        DELETE FROM DELIVERY_FEE_PER_KM
        WHERE id = '{id}'
        """
    cursor.execute(SQL)

    return redirect('deliveryfeeperkm:show_deliveryfee')

def show_updatedeliveryfee(request):
    return render(request, 'updatedeliveryfeeperkm.html')

def show_createdeliveryfee(request):   
    return render(request, 'createdeliveryfeeperkm.html')