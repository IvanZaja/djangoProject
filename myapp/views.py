from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render


# Create your views here.
def index(request):
    title = 'Welcome to myapp!'
    return render(request, "index.html", {'title': title})

def about(request):
    username = 'IvanZS'
    return render(request, "about.html", {'username': username})

def hello(request, username):
    return HttpResponse("<h1>Hello, %s</h1>" % username)


def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def tasks(request):
    # task = Task.objects.get(id=id) # De esta forma NO salen las paginas 404
    # task = get_object_or_404(Task, id=id) # De esta forma SI salen las paginas 404
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {'tasks': tasks})