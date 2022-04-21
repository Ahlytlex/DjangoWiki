from django.shortcuts import render
from . import util

# Create your views here.

def index(request, name):
  
    if(util.get_entry(name)):
        return render(request, "wikiApp/index.html", {"view_name" : name})
