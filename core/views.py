from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm, TaskForm
from .models import Task
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required



def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/signup.html', {'form': form})

def task_list(request):
    query = request.GET.get('q')
    tasks = Task.objects.filter(title__icontains=query) if query else Task.objects.all()
    return render(request, 'core/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'core/task_form.html', {'form': form})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'core/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'core/task_confirm_delete.html', {'task': task})


# View to redirect users to the login page if not authenticated
def redirect_to_login(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to the login page if not logged in
    return redirect('task_list')  # Redirect to task list if user is authenticated
