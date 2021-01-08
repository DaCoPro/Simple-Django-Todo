from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', {'todos': todos})

class TodoCreate(CreateView):
    model = Todo
    fields = "__all__"

def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return redirect('/')