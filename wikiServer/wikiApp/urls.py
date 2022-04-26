from django.urls import path

from . import views

# create all url patterns - this one routes .../mysite/appname/index to the index function in your views file.
urlpatterns = [

    path('wiki/entry/<str:entryName>', views.index)

]