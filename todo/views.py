from django.shortcuts import get_object_or_404, render, redirect
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
    
def update(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == "POST":
        new_task_detail = request.POST.get("new_task")
        is_complete = request.POST.get("is_complete")
        task.is_complete = bool(is_complete)
        task.task_detail = new_task_detail
        task.save()
        return redirect("/")
    else:
        return render(request, "update_task.html", {"task": task})
    
def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect("/")
