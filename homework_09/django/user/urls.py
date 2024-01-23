from django.urls import path

from .views import SignInView, SignOutView, SignUpView

app_name = "user"

urlpatterns = [
    path("sign_in", SignInView.as_view(), name="sign_in"),
    path("sign_up", SignUpView.as_view(), name="sign_up"),
    path("sign_out", SignOutView.as_view(), name="sign_out"),
]
