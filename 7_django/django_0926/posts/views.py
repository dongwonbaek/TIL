from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
    # 모든 글 목록을 보여준다.
    # 1. DB에서 모든 글을 불러온다.
    # 2. template에 보내준다.
    posts = Post.objects.all()
    context = {"posts": posts}

    return render(request, "posts/index.html", context)


def new(request):
    return render(request, "posts/new.html")


def create(request):
    title = request.GET.get("title")
    content = request.GET.get("content")
    Post.objects.create(title=title, content=content)
    context = {
        "title": title,
        "content": content,
    }
    return redirect("posts:index")


def delete(request, pk):
    Post.objects.get(id=pk).delete()
    return redirect("posts:index")
