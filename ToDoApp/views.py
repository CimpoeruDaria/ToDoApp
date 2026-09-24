from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Task
from .forms import TaskForm

# Home view (login page)
def home_view(request):
    return render(request, 'ToDoApp/login.html')

# Main Page After Login 
def main_page_view(request):
    tasks = Task.objects.filter(user=request.user).order_by('-task_created_at')

    completed_count = 0
    overdue_count = 0
    in_progress_count = 0

    for task in tasks:
        if task.task_completed:
            completed_count += 1
        elif task.is_overdue:
            overdue_count += 1
        else:
            in_progress_count += 1

    total_tasks = tasks.count()

    context = {
        'tasks': tasks, 
        'completed_count': completed_count, 
        'overdue_count': overdue_count, 
        'in_progress_count': in_progress_count, 
        'total_tasks': total_tasks, 
    }
    return render(request, 'ToDoApp/main_page.html', context)

# Task create view
@login_required
def task_create_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit = False)
            task.user = request.user
            task.save()
            return redirect('main_page')
    else:
        form = TaskForm()

    tasks = Task.objects.filter(user = request.user).order_by('-task_created_at')
    return render(request, 'ToDoApp/task_create.html', {
        'form': form, 
        'tasks': tasks 
        })

# Delete task
@login_required
def task_delete_view(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('main_page')
    return render(request, 'ToDoApp/task_confirm_delete.html', {'task': task})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main_page')
    else:
        form = UserCreationForm()
    return render(request, 'ToDoApp/register.html', {'form': form})    

# Update main page after checking a task 
def task_toggle_complete_view(request, task_id):
    task = get_object_or_404(Task, id = task_id, user = request.user)
    task.task_completed = not task.task_completed
    task.save()
    return redirect('main_page')

    