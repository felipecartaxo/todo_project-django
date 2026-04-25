from django.db import models

# representa uma tarefa simples
# e armazena-a no banco
class Todo(models.Model):
    
    # define um campo 'title' do tipo CharField
    # com limite de 200 caracteres
    title = models.CharField(max_length=200)

    # ao retornar o objeto,
    # retorna o valor do campo 'title'
    def __str__(self):
        return self.title