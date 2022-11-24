from django.shortcuts import render

# Create your views here.
def transaction_courier(request):
    return render(request, 'transaction_courier.html', {})