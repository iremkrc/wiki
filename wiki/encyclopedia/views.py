
from django.shortcuts import render, redirect
from django import forms
from . import util
import markdown2
import random as rd

class SearchForm(forms.Form):
    field = forms.CharField()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, name):
    if name in util.list_entries():
        return render(request,"encyclopedia/entry.html", {
            "name": name,
            "content": markdown2.markdown(util.get_entry(name))
        })
    else:
        return render(request,"encyclopedia/error.html", {
            "message": "Page not found."
        })

def search(request):
    entry_name = request.POST.get('q')
    if entry_name in util.list_entries():
        return redirect(f"wiki/{entry_name}")
    else:
        search_list = []
        for entry in util.list_entries():
            if entry_name in entry:
                search_list.append(entry)
        return render(request, "encyclopedia/search.html", {
            "entries": search_list
        })

    
def create(request):
    return render(request, "encyclopedia/create.html")

def new(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    if title in util.list_entries():
        return render(request, "encyclopedia/error.html", {
            "message": "Entry already exists."
        })
    else:
        util.save_entry(title, content)
        return redirect(f"wiki/{title}")

def edit(request, title):
    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "content": util.get_entry(title)
    })

def save(request, title):
    content = request.POST.get('edit')
    util.save_entry(title, content)
    return redirect(f"../{title}")

def random(request):
    random_entry = rd.choice(util.list_entries())
    return redirect(f"wiki/{random_entry}")
