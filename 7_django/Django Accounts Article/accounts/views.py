from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from .models import User
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)

def index(request):
    users = User.objects.all()
    context = {
        'users': users,
    }

    return render(request, 'accounts/index.html', context)

def detail(request, pk):
    user = User.objects.get(pk=pk)
    context = {
        'user':user,
    }
    return render(request, 'accounts/detail.html', context)