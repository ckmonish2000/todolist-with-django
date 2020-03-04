from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    a={1:"hello",2:"hey"}
    context={"a" : a}
    return render(request,"index.html",context)

def fid(request,flightid) :
    return render(request,"pst.htm")



def pst(request):
    if request.method=="POST":
        print(request.POST)
    return HttpResponse("works")