from django.urls import path
from .import views 
urlpatterns = [
    path("",views.index,name="hello"),
    path("<str:itm>",views.dels)

]