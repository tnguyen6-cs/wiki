from django.shortcuts import render, redirect
from markdown2 import markdown
from . import util
from django.http import HttpResponse
from django import forms

class Search(forms.Form):
    item = forms.CharField(widget=forms.TextInput(attrs={'class' : 'myfieldclass', 'placeholder': 'Search'}))
def index(request):
    if request.GET.get('q'):
        query = request.GET.get("q", "")
        return(search(request, query))
    else:
        return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
        })

def entry(request,entry):
    if util.get_entry(entry)==None:
        return HttpResponse("This entry does not exist.")
    content=markdown(util.get_entry(entry))
    return render(request,"encyclopedia/entry.html",{"entry":entry,"content":content})

def search(request,query):
    entries = util.list_entries()
    results=[]
    for entry in entries:
        if query.lower() == entry.lower():
            content=markdown(util.get_entry(query))
            return render(request,"encyclopedia/entry.html",{"entry":entry,"content":content})
        if query.lower() in entry.lower():
            results.append(entry)
    return render(request, "encyclopedia/search.html", {"entries": results,})


