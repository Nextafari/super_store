from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib import messages
from .forms import SignUpForm


# Create your views here.

def login(request):
    return render(request, 'index.html', {})


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, f"Sign up successful {username}")
            return redirect('main:login')
    
    else:
        form = SignUpForm()
        return render(request, 'sign_up.html', {'form': form})



def login_request():
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return messages.success(request, f"welcome back {username}")
    else:
        return messages.warning(request, f"Invalid username or password")


        
