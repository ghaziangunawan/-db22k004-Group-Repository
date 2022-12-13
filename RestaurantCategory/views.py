from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import connection

ssp = 'set search_path to sirest'

# Create your views here.
def rest_category_create(request):
    if request.method == 'POST':
        rest_cat_name = request.POST.get('rest_cat_name')

        cursor = connection.cursor()
        cursor.execute(ssp)

        sql = f"""
        SELECT MAX(CAST(Id as NUMERIC)) FROM RESTAURANT_CATEGORY
        """
        
        cursor.execute(sql)
        max_id = cursor.fetchone()

        rest_cat_id = 1
        if max_id[0]:
            rest_cat_id = int(max_id[0]) + 1

        sql = f"""
        INSERT INTO RESTAURANT_CATEGORY VALUES
        ({rest_cat_id}, '{rest_cat_name}')
        """

        cursor.execute(sql)

        return redirect('RestaurantCategory:rest_category_read')

    return render(request, 'rest_category_create.html')

def rest_category_read(request):
    cursor = connection.cursor()
    cursor.execute(ssp)

    sql = f"""
    SELECT Id, Name, COUNT(RCategory)
    FROM RESTAURANT_CATEGORY
    LEFT JOIN RESTAURANT
    ON Id = RCategory
    GROUP BY Id, Name
    ORDER BY CAST(Id as NUMERIC)
    """

    cursor.execute(sql)
    data = cursor.fetchall()

    context = {
        'rest_cat': data,
    }

    return render(request, 'rest_category_read.html', context)

def delete_rest_cat(request, rest_cat_id):
    cursor = connection.cursor()
    cursor.execute(ssp)

    sql = f"""
    DELETE FROM RESTAURANT_CATEGORY WHERE Id = '{rest_cat_id}'
    """
    
    cursor.execute(sql)

    return HttpResponseRedirect(reverse('RestaurantCategory:rest_category_read'))