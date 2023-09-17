from django.shortcuts import render, redirect
from todo.models import Task

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    return render(request, "index.html", {"tasks":tasks})

def create_task(request):
    if request.method == "POST":
        task_detail = request.POST["new_task"]
        task = Task.objects.create(task_detail=task_detail)
        task.save()
        return redirect("/")
    else:
        return render(request, "createTask.html")