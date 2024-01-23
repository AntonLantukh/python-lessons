from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages

from .forms import SigninForm, SignupForm

# Create your views here.


class SignInView(LoginView):
    template_name = "sign_in.html"
    form_class = SigninForm
    redirect_authenticated_user = reverse_lazy("tasks:list")


class SignOutView(LogoutView):
    pass


class SignUpView(CreateView):
    template_name = "sign_up.html"
    form_class = SignupForm

    def form_valid(self, form):
        form.save()

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")

        user = authenticate(self.request, username=username, password=password)

        login(self.request, user)

        messages.success(self.request, "Registration successful")
        return redirect("tasks:list")
