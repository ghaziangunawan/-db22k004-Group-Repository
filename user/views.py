from django.shortcuts import render
from django.shortcuts import render, redirect
from django.db import connection
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def show_register(request):   
    return render(request, 'register.html')

def show_adminform(request):
    errors = []
    cursor = connection.cursor()
    search_path =  "set search_path to sirest"
    cursor.execute(search_path)
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')  
        name = request.POST.get('name')
        if email and password and  name and phone:
            SQL = f"""
                SELECT EXISTS (
                    SELECT *
                    FROM USER_acc
                    WHERE email='{email}'
                )
                """
            cursor.execute(SQL)
            isFound = cursor.fetchone()[0]
            if not isFound:
                user = (email,password,phone,name.split()[0],name.split()[1])
                SQL = f"""
                    INSERT INTO user_acc VALUES
                    {user}
                    """
                try:
                    cursor.execute(SQL)
                    SQL = f"""
                    INSERT INTO ADMIN VALUES
                    ('{email}')
                    """
                    cursor.execute(SQL)

                    return redirect('loginlogout:show_login')
                except:
                    errors.append("""
                        Please make sure that the password 
                        contains at least 1 capital letter
                        and 1 number
                        """)
            else:
                errors.append("{email} has already have an user account")
        else:
            errors.append("All fields must be filled")

    context = {'errors':errors}
    return render(request,'admin_form.html',context)

def show_customerform(request):
    errors = []
    cursor = connection.cursor()
    search_path =  "set search_path to sirest"
    cursor.execute(search_path)
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        nik = request.POST.get('nik')
        bank = request.POST.get('bank')
        accnum = request.POST.get('accnum')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        print(email)
        print(password)
        print(name)
        print(phone)
        print(nik)
        print(bank)
        print(accnum)
        print(dob)
        print(gender)

        if email and password and name and phone and nik and bank and accnum and dob and gender:
            print('a')
            SQL = f"""
                SELECT EXISTS (
                    SELECT *
                    FROM USER_acc
                    WHERE email='{email}'
                )
                """
            cursor.execute(SQL)
            isFound = cursor.fetchone()[0]
            if not isFound:
                print('b')
                user = (email,password,phone,name.split()[0],name.split()[1])
                SQL = f"""
                    INSERT INTO user_acc VALUES
                    {user}
                    """
                try:
                    print('c')
                    cursor.execute(SQL)
                    print('a132')
                    admin = 'hgelderts@wunderground.com'
                    transaction_actor = (email,nik,bank,accnum,0,admin)
                    SQL = f"""
                    INSERT INTO TRANSACTION_ACTOR VALUES
                    {transaction_actor}
                    """
                    cursor.execute(SQL)
                    print('a12')

                    customer = (email,dob,gender)
                    SQL = f"""
                        INSERT INTO CUSTOMER VALUES
                        {customer}
                        """
                    cursor.execute(SQL)
                    print('a13')
                    return redirect('loginlogout:show_login')
                except:
                    print('d')
                    errors.append("""
                        Please make sure that the password 
                        contains at least 1 capital letter
                        and 1 number
                        """)
            else:
                print('e')
                errors.append("{email} has already have an user account")
        else:
            print('f')
            errors.append("All fields must be filled")
    context = {'errors':errors}
    return render(request,'register_customer.html',context)

def show_restaurantform(request):
    errors = []
    cursor = connection.cursor()
    search_path =  "set search_path to sirest"
    cursor.execute(search_path)
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password') 
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        nik = request.POST.get('nik')
        bank = request.POST.get('bank')
        accnum = request.POST.get('accnum')
        resname = request.POST.get('resname')
        branch = request.POST.get('branch')
        phonenum = request.POST.get('phonenum')
        street = request.POST.get('street')
        district = request.POST.get('district')
        city = request.POST.get('city')
        province = request.POST.get('province')
        category = request.POST.get('category')  
        print(email)
        print(password)
        print(name)
        print(phone)
        print(nik)
        print(bank)
        print(accnum)
        print(resname)
        print(branch)
        print(phonenum)
        print(street)
        print(district)
        print(city)
        print(province)
        print(category)
        if email and password and name and phone and nik and bank and accnum and resname and branch and phonenum and street and district and city and province and category:
            SQL = f"""
                SELECT EXISTS (
                    SELECT *
                    FROM USER_acc
                    WHERE email='{email}'
                )
                """
            cursor.execute(SQL)
            isFound = cursor.fetchone()[0]
            if not isFound:
                user = (email,password,phone,name.split()[0],name.split()[1])
                SQL = f"""
                    INSERT INTO user_acc VALUES
                    {user}
                    """
                try:
                    cursor.execute(SQL)
                    admin = 'hgelderts@wunderground.com'
                    transaction_actor = (email,nik,bank,accnum,0,admin)
                    SQL = f"""
                    INSERT INTO TRANSACTION_ACTOR VALUES
                    {transaction_actor}
                    """
                    cursor.execute(SQL)
                    print('a12')
                    restaurant = (resname,branch,email,phonenum,street,district,city,province,10,category)
                    SQL = f"""
                    INSERT INTO RESTAURANT VALUES
                    {restaurant}
                    """
                    cursor.execute(SQL)
                    return redirect('loginlogout:show_login')
                except:
                    errors.append("""
                        Please make sure that the password 
                        contains at least 1 capital letter
                        and 1 number
                        """)
                    
            else:
                errors.append("{email} has already have an user account")
        else:
            errors.append("All fields must be filled")
    SQL = f"""
    SELECT * FROM RESTAURANT_CATEGORY
    """
    cursor.execute(SQL)
    rcategory = cursor.fetchall()
    
    context = {'errors':errors,'rcategory':rcategory}
    return render(request,'register_rest.html',context)
    

def show_courierform(request):
    errors = []
    cursor = connection.cursor()
    search_path =  "set search_path to sirest"
    cursor.execute(search_path)
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password') 
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        nik = request.POST.get('nik')
        bank = request.POST.get('bank')
        accnum = request.POST.get('accnum')
        plate = request.POST.get('plate')
        lisence = request.POST.get('lisence') 
        type = request.POST.get('type')
        brand = request.POST.get('brand')

        if email and password and name and phone and nik and bank and accnum and plate and lisence and type and brand:
            SQL = f"""
                SELECT EXISTS (
                    SELECT *
                    FROM USER_acc
                    WHERE email='{email}'
                )
                """
            cursor.execute(SQL)
            isFound = cursor.fetchone()[0]
            if not isFound:
                user = (email,password,phone,name.split()[0],name.split()[1])
                SQL = f"""
                    INSERT INTO user_acc VALUES
                    {user}
                    """
                try:
                    cursor.execute(SQL)
                    admin = 'hgelderts@wunderground.com'
                    transaction_actor = (email,nik,bank,accnum,0,admin)
                    SQL = f"""
                    INSERT INTO TRANSACTION_ACTOR VALUES
                    {transaction_actor}
                    """
                    cursor.execute(SQL)
                    courier = (email,plate,lisence,type,brand)
                    SQL = f"""
                    INSERT INTO COURIER VALUES
                    {courier}
                    """
                    cursor.execute(SQL)
                    return redirect('loginlogout:show_login')
                except:
                    errors.append("""
                        Please make sure that the password 
                        contains at least 1 capital letter
                        and 1 number
                        """)
            else:
                errors.append("{email} has already have an user account")
        else:
            errors.append("All fields must be filled")
    context = {'errors':errors}
    return render(request,'Courier_registration.html',context)

def show_userdashboard(request):
    return render(request, 'userdashboard.html')

def show_userdashboardtable(request):
    return render(request, 'UserDashboardwithtable.html')

def show_userprofile(request):
    return render(request, 'userprofile.html')