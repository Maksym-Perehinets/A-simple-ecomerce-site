from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class UserLoginView(LoginView):
    template_name = 'users/signin.html'
    form_class = AuthenticationForm

