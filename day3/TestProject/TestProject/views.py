from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def home(request):
    val=10+20
    return HttpResponse("<h2>Spam</h2>")

def navber(request):
    return render(request,"index.html")
    
def about(request):
    d={"name":"spam", "age":11,"arr":[1,2,3,4,5,6,7,8]}
    return render(request,"index.html",d)

#ex1

# def test(request):
#     val=[1,2,3,4,5,6,7,8]
#     s="django"
#     a="my first dtl"
#     return render(request,"test.html",{"list":val,"string":s,"str2":a})


#example 2

# def test(request):
#     val=[1,2,3,4,5,6,7,8]
#     s="django"
#     a="my first dtl"
#     x="AFRWJOSDFSLKDFJERWIO"
#     y="askdhiufhiouhklfcdaf"
#     dic={"list":val,"string":s,"str2":a,"str3":x,"str4":y}
#     return render(request,"test.html",dic)

def test(request):
    dt=datetime.datetime.now()
    return render(request,"test.html",{"dt":dt})

