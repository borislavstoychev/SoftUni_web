from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

from templates_advanced.core.mixins import BootstrapFormMixin

UserModel = get_user_model()


class SignUpForm(BootstrapFormMixin, UserCreationForm):

    class Meta:
        model = UserModel
        fields = ("email",)


class SignInForm(BootstrapFormMixin, AuthenticationForm):

    user = None

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if email is not None and password:
            self.user_cache = authenticate(self.request, email=email, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

