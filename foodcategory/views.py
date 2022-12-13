from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
import datetime
from django.db import connection
from random import randint
from django.core.exceptions import PermissionDenied



def add_food_category(request):
    if not request.session.get('isLoggedIn'): 
        return redirect('loginlogout:show_login')
    if not request.session.get('isAdmin'): 
        raise PermissionDenied()
    context = {}

    cursor = connection.cursor()
    search_path = 'set search_path to sirest'
    cursor.execute(search_path)

    if request.method == "POST":
        sql2 = f"""
        SELECT MAX(CAST(Id AS NUMERIC)) FROM FOOD_CATEGORY
        """
        
        cursor.execute(sql2)
        max_id = cursor.fetchone()

        fc_id = 1
        if max_id[0]:
            fc_id = int(max_id[0]) + 1
        unique_id = str(fc_id)

        food_category_name = request.POST.get("food_category")
        SQL = f"""INSERT INTO FOOD_CATEGORY VALUES
            ('{unique_id}', '{food_category_name}')
        """

        cursor.execute(SQL)

        return redirect("/foodcategory/")

    return render(request, "createfoodcategory.html", context)


def show_food_category(request):
    if not request.session.get('isLoggedIn'): 
        return redirect('loginlogout:show_login')
    if not request.session.get('isAdmin'): 
        raise PermissionDenied()

    cursor = connection.cursor()
    search_path = 'set search_path to sirest'
    cursor.execute(search_path)
    SQL= f"""SELECT name FROM FOOD_CATEGORY """
    cursor.execute(SQL)   

    food_category = cursor.fetchall()
    context = {"category":food_category}

    return render(request, "foodcategorylist.html", context)


def delete_food_category(request, name):
    if not request.session.get('isLoggedIn'): 
        return redirect('loginlogout:show_login')
    if not request.session.get('isAdmin'): 
        raise PermissionDenied()
        
    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO SIREST")
        cursor.execute(
            f"""
            DELETE FROM FOOD_CATEGORY
            WHERE name = '{name}'
        """
        )

        return redirect("/foodcategory/")
