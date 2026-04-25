from django.shortcuts import render, redirect
from .models import Todo

def todo_list(request): 
    todos = Todo.objects.all()

    if request.method == "POST":
        # cria tarefa
        if "add_task" in request.POST:
            title = request.POST.get("title")
            if title:
                Todo.objects.create(title=title)
            return redirect("todo_list")
        
    
