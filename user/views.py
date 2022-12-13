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
                    transaction_actor = (email,nik,bank,accnum,0)
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
                    transaction_actor = (email,nik,bank,accnum,0)
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
                    transaction_actor = (email,nik,bank,accnum,0)
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

def show_customerdashboard(request):
    cursor = connection.cursor()
    search_path =  "set search_path to PUBLIC"
    cursor.execute(search_path)
    email = request.session.get('useremail')
    search_path =  "set search_path to SIREST"
    cursor.execute(search_path)
    SQL = f"""
    SELECT * FROM USER_ACC WHERE email = '{email}'
    """
    cursor.execute(SQL)
    user = cursor.fetchall()[0]
    SQL = f"""
    SELECT * FROM TRANSACTION_ACTOR WHERE email = '{email}'
    """
    cursor.execute(SQL)
    transaction_actor = cursor.fetchall()[0]
    SQL = f"""
    SELECT * FROM CUSTOMER WHERE email = '{email}'
    """
    cursor.execute(SQL)
    customer = cursor.fetchall()[0]

    usremail,password,name,phone,nik,bank,accnum = user[0],user[1],str(user[3]) + ' ' + str(user[4]),user[2],transaction_actor[1],transaction_actor[2],transaction_actor[3]
    dob,gender = customer[1],customer[2]

    verified=False
    admin = None
    if transaction_actor[5]:
        admin = transaction_actor[5]
        verified = True
    restopay = transaction_actor[4]
    context = {'usremail': usremail,'password': password,'name': name,'phone': phone,'nik': nik,'bank': bank,'accnum': accnum,'dob': dob,'gender': gender,'verified': verified,'admin': admin,'restopay': restopay}
    return render(request,'customerdashboard.html',context)

def show_restaurantdashboard(request):
    cursor = connection.cursor()
    search_path =  "set search_path to PUBLIC"
    cursor.execute(search_path)
    email = request.session.get('useremail')
    search_path =  "set search_path to SIREST"
    cursor.execute(search_path)
    SQL = f"""
    SELECT * FROM USER_ACC WHERE email = '{email}'
    """
    cursor.execute(SQL)
    user = cursor.fetchall()[0]
    SQL = f"""
    SELECT * FROM TRANSACTION_ACTOR WHERE email = '{email}'
    """
    cursor.execute(SQL)
    transaction_actor = cursor.fetchall()[0]
    SQL = f"""
    SELECT * FROM RESTAURANT join restaurant_category on rcategory=id WHERE email = '{email}'
    """
    cursor.execute(SQL)
    restaurant = cursor.fetchall()[0]
    usremail,password,name,phone,nik,bank,accnum = user[0],user[1],str(user[3]) + ' ' + str(user[4]),user[2],transaction_actor[1],transaction_actor[2],transaction_actor[3]

    SQL = f"""
    SELECT * FROM restaurant_operating_hours WHERE name = '{restaurant[0]}' and branch = '{restaurant[1]}'
    """
    cursor.execute(SQL)
    ophours = cursor.fetchall()
    print(ophours)

    rname,rbranch,rphone,street,district,city,province,rating,category = restaurant[0],restaurant[1],restaurant[3],restaurant[4],restaurant[5],restaurant[6],restaurant[7],restaurant[8],restaurant[11]
    operating_hours = []
    for i in ophours:
        operating_hours.append([i[2],i[3],i[4]])
    print(operating_hours)

    verified=False
    admin = None
    if transaction_actor[5]:
        admin = transaction_actor[5]
        verified = True
    restopay = transaction_actor[4]
    context = {'usremail': usremail,'password': password, 'name': name,'phone': phone,'nik': nik,'bank': bank,'accnum': accnum,'rname': rname,'rbranch': rbranch,'rphone':rphone,'street':street,'district':district,'city':city,'province':province,'rating':rating,'category':category,'ophours':operating_hours,'verified': verified,'admin': admin,'restopay': restopay}
    return render(request,'restaurantdashboard.html',context)

def show_courierdashboard(request):
    cursor = connection.cursor()
    search_path =  "set search_path to PUBLIC"
    cursor.execute(search_path)
    email = request.session.get('useremail')
    search_path =  "set search_path to SIREST"
    cursor.execute(search_path)
    SQL = f"""
    SELECT * FROM USER_ACC WHERE email = '{email}'
    """
    cursor.execute(SQL)
    user = cursor.fetchall()[0]
    SQL = f"""
    SELECT * FROM TRANSACTION_ACTOR WHERE email = '{email}'
    """
    cursor.execute(SQL)
    transaction_actor = cursor.fetchall()[0]
    SQL = f"""
    SELECT * FROM COURIER WHERE email = '{email}'
    """
    cursor.execute(SQL)
    courier = cursor.fetchall()[0]

    usremail,password,name,phone,nik,bank,accnum = user[0],user[1],str(user[3]) + ' ' + str(user[4]),user[2],transaction_actor[1],transaction_actor[2],transaction_actor[3]
    plate,lisence,type,brand = courier[1],courier[2],courier[3],courier[4]

    verified=False
    admin = None
    if transaction_actor[5]:
        admin = transaction_actor[5]
        verified = True
    restopay = transaction_actor[4]
    context = {'usremail': usremail,'password': password,'name': name,'phone': phone,'nik': nik,'bank': bank,'accnum': accnum,'plate': plate,'lisence': lisence,'type':type,'brand':brand,'verified': verified,'admin': admin,'restopay': restopay}
    return render(request,'courierdashboard.html',context)

def show_admindashboard(request):
    cursor = connection.cursor()
    search_path =  "set search_path to PUBLIC"
    cursor.execute(search_path)
    email = request.session.get('useremail')
    search_path =  "set search_path to SIREST"
    cursor.execute(search_path)
    SQL = f"""
    SELECT * FROM USER_ACC WHERE email = '{email}'
    """
    cursor.execute(SQL)
    user = cursor.fetchall()[0]
   
    SQL = f"""
    select fname,lname,transaction_Actor.email,adminid
    from transaction_actor join user_Acc on transaction_Actor.email = user_Acc.email
    """
    cursor.execute(SQL)
    transaction_Actor = cursor.fetchall()
    print(transaction_Actor)
    usremail,password,name,phone = user[0],user[1],str(user[3]) + ' ' + str(user[4]),user[2]
    SQL = f"""
    select email
    from customer
    """
    cursor.execute(SQL)
    customer = cursor.fetchall()
    customerlist = []
    for i in customer:
        customerlist.append(i[0])
    SQL = f"""
    select email
    from restaurant
    """
    cursor.execute(SQL)
    restaurant = cursor.fetchall()
    restaurantlist = []
    for i in restaurant:
        restaurantlist.append(i[0])
    print(restaurantlist)
    SQL = f"""
    select email
    from courier
    """
    cursor.execute(SQL)
    courier = cursor.fetchall()
    courierlist = []
    for i in courier:
        courierlist.append(i[0])
    print(courierlist)
    print(transaction_Actor)
    print(customer)
    transaction_role = []
    for i in transaction_Actor:
        roles = ''
        print(i[2])
        if i[2] in customerlist:
            roles = 'customer'
        elif i[2] in restaurantlist:
            roles = "restaurant"
        elif i[2] in courierlist:
            roles = "courier"
        transaction_role.append(roles)
    

    for i in range(len(transaction_role)):
        transaction_Actor[i] = transaction_Actor[i] + (transaction_role[i],)
    
    print(transaction_Actor)

    context = {'usremail': usremail,'password': password,'name': name,'phone': phone,'actors':transaction_Actor}
    return render(request,'admindashboard.html',context)


def show_userprofile(request,role,email):
    cursor = connection.cursor()
    if role =='customer':
        search_path =  "set search_path to SIREST"
        cursor.execute(search_path)
        SQL = f"""
        SELECT * FROM USER_ACC WHERE email = '{email}'
         """
        cursor.execute(SQL)
        user = cursor.fetchall()[0]
  
        SQL = f"""
    SELECT * FROM TRANSACTION_ACTOR WHERE email = '{email}'
    """
        cursor.execute(SQL)
        transaction_actor = cursor.fetchall()[0]
        SQL = f"""
    SELECT * FROM CUSTOMER WHERE email = '{email}'
    """
        cursor.execute(SQL)
        customer = cursor.fetchall()[0]

        usremail,password,name,phone,nik,bank,accnum = user[0],user[1],str(user[3]) + ' ' + str(user[4]),user[2],transaction_actor[1],transaction_actor[2],transaction_actor[3]
        dob,gender = customer[1],customer[2]

        verified=False
        admin = None
        if transaction_actor[5]:
            admin = transaction_actor[5]
            verified = True
        restopay = transaction_actor[4]
        context = {'usremail': usremail,'password': password,'name': name,'phone': phone,'nik': nik,'bank': bank,'accnum': accnum,'dob': dob,'gender': gender,'verified': verified,'admin': admin,'restopay': restopay}
        return render(request,'customerprofile.html',context)
    

    elif role == 'restaurant':
        search_path =  "set search_path to SIREST"
        cursor.execute(search_path)
        SQL = f"""
    SELECT * FROM USER_ACC WHERE email = '{email}'
    """
        cursor.execute(SQL)
        user = cursor.fetchall()[0]
        SQL = f"""
    SELECT * FROM TRANSACTION_ACTOR WHERE email = '{email}'
    """
        cursor.execute(SQL)
        transaction_actor = cursor.fetchall()[0]
        SQL = f"""
    SELECT * FROM RESTAURANT join restaurant_category on rcategory=id WHERE email = '{email}'
    """
        cursor.execute(SQL)
        restaurant = cursor.fetchall()[0]
        usremail,password,name,phone,nik,bank,accnum = user[0],user[1],str(user[3]) + ' ' + str(user[4]),user[2],transaction_actor[1],transaction_actor[2],transaction_actor[3]

        SQL = f"""
    SELECT * FROM restaurant_operating_hours WHERE name = '{restaurant[0]}' and branch = '{restaurant[1]}'
    """
        cursor.execute(SQL)
        ophours = cursor.fetchall()

        rname,rbranch,rphone,street,district,city,province,rating,category = restaurant[0],restaurant[1],restaurant[3],restaurant[4],restaurant[5],restaurant[6],restaurant[7],restaurant[8],restaurant[11]
        operating_hours = []
        for i in ophours:
            operating_hours.append([i[2],i[3],i[4]])

        verified=False
        admin = None
        if transaction_actor[5]:
            admin = transaction_actor[5]
            verified = True
        restopay = transaction_actor[4]
        context = {'usremail': usremail,'password': password, 'name': name,'phone': phone,'nik': nik,'bank': bank,'accnum': accnum,'rname': rname,'rbranch': rbranch,'rphone':rphone,'street':street,'district':district,'city':city,'province':province,'rating':rating,'category':category,'ophours':operating_hours,'verified': verified,'admin': admin,'restopay': restopay}
        return render(request,'restaurantprofile.html',context)
    
    elif role == 'courier':
        search_path =  "set search_path to SIREST"
        cursor.execute(search_path)
        SQL = f"""
    SELECT * FROM USER_ACC WHERE email = '{email}'
    """
        cursor.execute(SQL)
        user = cursor.fetchall()[0]
        SQL = f"""
    SELECT * FROM TRANSACTION_ACTOR WHERE email = '{email}'
    """
        cursor.execute(SQL)
        transaction_actor = cursor.fetchall()[0]
        SQL = f"""
    SELECT * FROM COURIER WHERE email = '{email}'
    """
        cursor.execute(SQL)
        courier = cursor.fetchall()[0]

        usremail,password,name,phone,nik,bank,accnum = user[0],user[1],str(user[3]) + ' ' + str(user[4]),user[2],transaction_actor[1],transaction_actor[2],transaction_actor[3]
        plate,lisence,type,brand = courier[1],courier[2],courier[3],courier[4]

        verified=False
        if transaction_actor[5]:
            admin = transaction_actor[5]
            verified = True
        restopay = transaction_actor[4]
        context = {'usremail': usremail,'password': password,'name': name,'phone': phone,'nik': nik,'bank': bank,'accnum': accnum,'plate': plate,'lisence': lisence,'type':type,'brand':brand,'verified': verified,'admin': admin,'restopay': restopay}
        return render(request,'courierprofile.html',context)

def verification(request,email):
    cursor = connection.cursor()
    search_path =  "set search_path to sirest"
    cursor.execute(search_path)
    admin = 'kdoggrellf@taobao.com'
    SQL = f"""
    UPDATE TRANSACTION_ACTOR
    set adminid = '{admin}'
    where email = '{email}'
    """
    cursor.execute(SQL)

    return HttpResponseRedirect(reverse('user:show_admindashboard'))


