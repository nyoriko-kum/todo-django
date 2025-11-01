from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

def index(request):
    todos = Todo.objects.all()
    return render(request, 'todos/index.html', {'todos': todos})

def create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'todos/form.html', {'form': form})

def update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'todos/form.html', {'form': form})

def delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('index')
