# I have created this file!!
from django.http import HttpResponse
from django.shortcuts import render, redirect
import mysql.connector as sql 

# Declaring the Variables for Form(registration Function)!!
fn = ''
ln = ''
g = ''
em= ''
pwd= ''
def registration(request):
    global fn,ln,g,em,pwd
    if request.method=='POST':
        mydb = sql.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "DJANGO_TEST"
        )
        cursor = mydb.cursor()
        data = request.POST
        for key, value in data.items():
            if key == "first_name":
                fn = value
            if key == "last_name":
                ln = value
            if key == "Gender":
                g = value
            if key == "email":
                em = value
            if key == "password":
                pwd = value

        # Validation Of Form!!
        if(not fn):
            return render(request,('form_registration.html')) 
        elif(not ln):
            return render(request,('form_registration.html'))
        elif(not g):
            return render(request,('form_registration.html'))
        elif(not em):
            return render(request,('form_registration.html'))
        elif(not pwd):
            return render(request,('form_registration.html'))
        else:   
            data_insert = "INSERT INTO FORM VALUES('{}','{}','{}','{}','{}')".format(fn,ln,g,em,pwd)
            cursor.execute(data_insert)
            mydb.commit()

            return render(request,'success.html')
    else:
        return render(request,('form_registration.html'))

def success(request):
    return render(request,('success.html'))




