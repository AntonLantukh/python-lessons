from django.forms import CharField, PasswordInput, ModelForm, TextInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget = TextInput(attrs={"class": "form-control"})
        self.fields["password1"].widget = PasswordInput(attrs={"class": "form-control"})
        self.fields["password2"].widget = PasswordInput(attrs={"class": "form-control"})


class SigninForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget = TextInput(attrs={"class": "form-control"})
        self.fields["password"].widget = PasswordInput(attrs={"class": "form-control"})
