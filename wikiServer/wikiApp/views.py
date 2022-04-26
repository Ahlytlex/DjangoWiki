from django.shortcuts import render
from . import util

# Create your views here.

def index(request,entryName):
  
    if(util.get_entry(entryName)):
        return render(request, "wikiApp/index.html", {"view_name" : entryName
        , "entry_contents" : util.get_entry(entryName)})
    else:
        return render(request, "wikiApp/404.html")

