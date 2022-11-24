from django.shortcuts import render

# Create your views here.

def show_register(request):   
    return render(request, 'register.html')

def show_adminform(request):   
    return render(request, 'admin_form.html')

def show_customerform(request):
    return render(request, 'register_customer.html')

def show_restaurantform(request):   
    return render(request, 'register_rest.html')

def show_courierform(request):
    return render(request, 'Courier_registration.html')

def show_userdashboard(request):
    return render(request, 'userdashboard.html')

def show_userdashboardtable(request):
    return render(request, 'UserDashboardwithtable.html')

def show_userprofile(request):
    return render(request, 'userprofile.html')