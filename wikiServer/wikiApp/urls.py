from django.urls import path

from . import views

# create all url patterns - this one routes .../mysite/appname/index to the index function in your views file.
app_name='wiki'
urlpatterns = [
    path('wiki/entry/goHome', views.goHome, name='goHome'),
    path('wiki/entry/savePage', views.savePage, name='savePage'),
    path('wiki/entry/randPage', views.rand_page, name='randPage'),
    path('wiki/entry/parsePage', views.post_response, name='parsePage'),
    path('wiki/entry/newPage', views.newPage, name='newPage'),
    path('wiki/entry/editPage/<str:entryName>', views.editPage, name='editPage'),
    path('wiki/entry/pageMan', views.pageMan, name='pageMan'),
    path('wiki/entry/<str:entryName>', views.index, name='entry'),
 

]