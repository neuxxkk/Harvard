from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
# Create your views here.
def index(request):
    if "tasks" not in request.session: #Se o usuario / request session não tiver já uma lista
        request.session["tasks"] = [] # O dê / crie uma nova

    return render(request, "tasks/index.html", {
        "tasks":request.session["tasks"]
 })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid(): # Se uma uma nova tarefa foi realmente enviada
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task] # Append similar
            return HttpResponseRedirect(reverse("tasks:index")) # Ao adicionar uma nova tarefa em add.html, volte para a lista(index.html)

        else:
            return render(request, "tasks/add.html", {
                "form":form
            })

    return render(request, "tasks/add.html", {
        "form":NewTaskForm(),
    })