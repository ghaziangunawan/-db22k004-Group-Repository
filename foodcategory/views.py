from django.shortcuts import render

# Create your views here.

def show_foodcategorylist(request):   
    return render(request, 'foodcategorylist.html')

def show_createfoodcategory(request):   
    return render(request, 'createfoodcategory.html')