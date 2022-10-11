from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
    }
    return render(request, "article/index.html", context)


def create(request):
    if request.method == "POST":
        article = ArticleForm(request.POST)
        if article.is_valid:
            article.save()
            return redirect("article:index")
    else:
        article = ArticleForm()
    context = {
        "article": article,
    }
    return render(request, "article/create.html", context)
