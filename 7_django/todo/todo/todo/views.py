from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Todo


def index(request):
    todo = Todo.objects.all().order_by("id")
    context = {
        "todos": todo,
    }
    return render(request, "todo/index.html", context)


def create(request):
    title = request.GET.get("title")
    content = request.GET.get("content___")
    priority = request.GET.get("priority")
    date = request.GET.get("date")
    Todo.objects.create(title=title, content=content, priority=priority, deadline=date)
    return redirect("todo:index")


def update(request, pk):
    completed_ = Todo.objects.get(id=pk)
    if completed_.completed == True:
        Todo.objects.filter(id=pk).update(completed=False)
    else:
        Todo.objects.filter(id=pk).update(completed=True)
    return redirect("todo:index")


def delete(request, pk):
    Todo.objects.get(id=pk).delete()
    return redirect("todo:index")


def detail(request, pk):
    detail = Todo.objects.get(id=pk)
    context = {
        "detail": detail,
    }
    return render(request, "todo/detail.html", context)


def edit(request, pk):
    edit = Todo.objects.get(id=pk)

    context = {
        "edit": edit,
    }
    return render(request, "todo/edit.html", context)


def change(request, pk):
    change = Todo.objects.get(id=pk)
    change.title = request.GET["title"]
    change.content = request.GET["content"]
    change.save()
    return redirect("todo:index")
