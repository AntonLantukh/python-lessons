from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

# Create your views here.


def sign_in(request):
    user_form = AuthenticationForm(data=request.POST or None)

    if request.method == "POST":
        if user_form.is_valid():
            username = user_form.cleaned_data["username"]
            password = user_form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect("tasks:list")
        else:
            print(user_form.non_field_errors())
            print(user_form.errors)

    return render(request, "sign_in.html", {"form": user_form})


def sign_up(request):
    user_form = UserCreationForm(data=request.POST or None)

    if request.method == "POST":
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data["username"]
            password = user_form.cleaned_data["password1"]

            user = authenticate(request, username=username, password=password)

            login(request, user)
            messages.success(request, "Registration successful")
            return redirect("tasks:list")

    return render(request, "sign_up.html", {"form": user_form})


def sign_out(request):
    logout(request)
    return redirect("home")
