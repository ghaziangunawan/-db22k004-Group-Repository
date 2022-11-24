from django.shortcuts import render

# Create your views here.
def show_operationalhours(request):   
    return render(request, 'operationalhours.html')

def show_operationalhourstime(request):   
    return render(request, 'operationalhourslist.html')

def show_edit(request):   
    return render(request, 'edit.html')
