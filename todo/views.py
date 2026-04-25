from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

def todo_list(request): 
    todos = Todo.objects.all()

    # se a requisição for
    # do tipo POST
    if request.method == "POST":
        
        # cria uma nova tarefa
        if "add_task" in request.POST:
            # coleta o title a partir
            # da requisição do form
            title = request.POST.get("title")
            if title:
                # cria e persiste o objeto
                # já com o 'title'
                Todo.objects.create(title=title)

            # após salvo, redireciona
            # para a tela de listagem
            return redirect("todo_list")
        
        # edita uma tarefa existente
        if "edit_task" in request.POST:
            # coleta os novos atributos
            # a partir do form
            task_id = request.POST.get("task_id")
            new_title = request.POST.get("new_title")
            
            # retorna a tarefa que queremos
            # atualizar a partir do id ou,
            # caso não exista, retorna NOT_FOUND
            todo = get_object_or_404(Todo, id = task_id)

            # altera os atributos da tarefa existente
            # que foi retornada no objeto 'todo'
            todo.title = new_title

            # persiste o objeto após
            # as atualizações do mesmo
            todo.save()

            # após salvo, redireciona
            # para a tela de listagem
            return redirect("todo_list")
        
        # remove uma tarefa existente
        if "delete_task" in request.POST:
            # coleta o id a partir
            # da requisição
            task_id = request.POST.get("task_id")

            # retorna a tarefa que queremos
            # remover a partir do id ou,
            # caso não exista, retorna NOT_FOUND
            todo = get_object_or_404(Todo, id = task_id)
            todo.delete()

            # após removido, redireciona
            # para a tela de listagem
            return redirect("todo_list")
        
        if "clear_all" in request.POST:
            # remove todos as instâncias
            # dos objetos do tipo Todo
            Todo.objects.all().delete()

            # após remover todas as tarefas,
            # redireciona para a tela de listagem
            return redirect("todo_list")
