from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    val=10+20
    return HttpResponse("<h2>Spam</h2>")

def navber(request):
    return render(request,"index.html")
    
def about(request):
    d={"name":"spam", "age":11,"arr":[1,2,3,4,5,6,7,8]}
    return render(request,"index.html",d)
