from . import views
from django.urls import path


urlpatterns = [
    path("",views.index),
    path("<int:flightid>",views.fid),
    path("post",views.pst)
]
