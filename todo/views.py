from django.shortcuts import render,HttpResponse,HttpResponseRedirect,reverse
from .models import todo
# Create your views here.
def index(request):
    if request.method=="POST":
        print(request.POST)
        itm=request.POST["item"]
        desc=request.POST["desc"]
        a=todo(item=itm,des=desc)
        a.save()
        print(todo.objects.all())
        print(itm,desc)
        return HttpResponseRedirect(reverse("hello"))
    items=todo.objects.all()
    wk="study"
    print(todo.objects.filter(item=wk))
    context={"stuff":items}
    return render(request,"index.htm",context)



def dels(request,itm):
    a=todo.objects.filter(item=itm)
    a.delete()
    return HttpResponseRedirect(reverse("hello"))
    
    
