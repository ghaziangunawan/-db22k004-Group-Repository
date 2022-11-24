from django.shortcuts import render

# Create your views here.
def ingredient_create(request):
    return render(request, 'ingredient_create.html')

def ingredient_read(request):
    return render(request, 'ingredient_read.html')