from django.shortcuts import render

# Create your views here.
def rest_category_create(request):
    return render(request, 'rest_category_create.html', {})

def rest_category_read(request):
    return render(request, 'rest_category_read.html')