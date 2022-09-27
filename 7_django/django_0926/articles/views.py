from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "articles/index.html")


def create(request):
    content = request.GET["content"]
    context = {
        "content": content,
    }
    return render(request, "articles/create.html", context)
