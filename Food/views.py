from django.shortcuts import render

# Create your views here.


def show_foodlist(request):   
    return render(request, 'showfoodlist.html')

def show_addfood(request):   
    return render(request, 'addfood.html')

def show_editfood(request):
    return render(request, 'editfood.html')

def show_restaurantlist(request):   
    return render(request, 'showrestaurantlist.html')

def show_restaurantmenu(request):
    return render(request, 'showrestaurantdetail.html')