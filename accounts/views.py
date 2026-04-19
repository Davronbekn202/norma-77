from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect

from firstapp.models import Product
from .forms import RegisterForm
from django.contrib.auth import get_user_model

User = get_user_model()

def home(request):
    return render(request,'success.html')

@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'student'
            user.save()

            return redirect('login')  # login sahifaga o‘tadi
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

def is_manager(user):
    return user.groups.filter(name="Managers").exists()

@login_required
@user_passes_test(is_manager)
def manager_panel(request):
    return render(request, "manager_panel.html")

