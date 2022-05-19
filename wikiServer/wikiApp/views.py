import markdown
import random
from turtle import title
from django.shortcuts import redirect, render
from . import util

# Create your views here.

def index(request,entryName):
  
    if(util.get_entry(entryName)):
        return render(request, "wikiApp/index.html", {"view_name" : entryName
        , "entry_contents" : markdown.markdown(util.get_entry(entryName))})
    else:
        return render(request, "wikiApp/404.html")

def post_response(request):
    if(request.method == "POST"):
        query=request.POST['EName']
        res = []
        list = util.list_entries()
        for i in list:
            if query in i:
                res.append(i)
            

        if(util.get_entry(query) != None):
            return redirect('/wiki/entry/' + query)
        
        else:
            return render(request, "wikiApp/404.html", {
                "empty" : len(res) == 0,
                "results" : res
            })



    else:
        print("Not a post")
        return render(request, "wikiApp/404.html")

def rand_page(request):
    curEntries = util.list_entries()
    randEntry = random.choice(curEntries)
    return redirect('/wiki/entry/' + randEntry)

def newPage(request):
        return render(request, 'wikiApp/add.html')

def editPage(request, entryName):
    if(util.get_entry(entryName)):
        return render(request, "wikiApp/edit.html", {"view_name" : entryName
        , "entry_contents" : util.get_entry(entryName)})

def pageMan(request):
    if(request.method == "POST"):
        title = request.POST['Title']
        content = request.POST['Content']
        util.save_entry(title,content)
        return redirect('wiki:entry', entryName=title)

def savePage(request):
    if(request.method == "POST"):
        title = request.POST['Title']
        content = request.POST['Content']
        util.save_entry(title,content)
        return redirect('wiki:entry', entryName=title)

def goHome(request):
        list = util.list_entries()
        return render(request, "wikiApp/home.html", {
                "results" : list
        })




