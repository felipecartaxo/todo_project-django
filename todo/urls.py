from django.urls import path
from . import views

# cria as rotas para o app 'todo'
urlpatterns = [
    path('', views.todo_list, name='todo_list'),

]