from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import connection
from django.core.exceptions import PermissionDenied
from django.views.decorators.csrf import csrf_exempt

ssp = 'set search_path to sirest'

# Create your views here.
@csrf_exempt
def ingredient_create(request):
    if not request.session.get('isLoggedIn'): return redirect('loginlogout:show_login')
    if not request.session.get('isAdmin'): raise PermissionDenied()

    if request.method == 'POST':
        ingredient_name = request.POST.get('ingredient_name')

        cursor = connection.cursor()
        cursor.execute(ssp)

        sql = f"""
        SELECT MAX(CAST(Id AS NUMERIC)) FROM INGREDIENT
        """
        
        cursor.execute(sql)
        max_id = cursor.fetchone()

        ingredient_id = 1
        if max_id[0]:
            ingredient_id = int(max_id[0]) + 1

        sql = f"""
        INSERT INTO INGREDIENT VALUES
        ({ingredient_id}, '{ingredient_name}')
        """

        cursor.execute(sql)

        return redirect('Ingredients:ingredient_read')

    return render(request, 'ingredient_create.html')

@csrf_exempt
def ingredient_read(request):
    if not request.session.get('isLoggedIn'): return redirect('loginlogout:show_login')
    if not request.session.get('isAdmin'): raise PermissionDenied()

    cursor = connection.cursor()
    cursor.execute(ssp)

    sql = f"""
    SELECT Id, Name, COUNT(FoodName)
    FROM INGREDIENT
    LEFT JOIN FOOD_INGREDIENT
    ON Id = Ingredient
    GROUP BY Id, Name
    ORDER BY CAST(Id as NUMERIC)
    """

    cursor.execute(sql)
    data = cursor.fetchall()

    context = {
        'ingredient': data,
    }

    return render(request, 'ingredient_read.html', context)

@csrf_exempt
def delete_ingredient(request, ingredient_id):
    if not request.session.get('isLoggedIn'): return redirect('loginlogout:show_login')
    if not request.session.get('isAdmin'): raise PermissionDenied()

    cursor = connection.cursor()
    cursor.execute(ssp)

    sql = f"""
    DELETE FROM INGREDIENT WHERE Id = '{ingredient_id}'
    """
    
    cursor.execute(sql)

    return HttpResponseRedirect(reverse('Ingredients:ingredient_read'))