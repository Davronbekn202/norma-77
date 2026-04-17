from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import get_user_model

User = get_user_model()

def home(request):
    return render(request,'success.html')

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()

            return redirect('login')  # login sahifaga o‘tadi
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})
