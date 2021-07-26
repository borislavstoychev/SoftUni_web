from django import forms

from templates_advanced.core.mixins import BootstrapFormMixin
from templates_advanced.profiles.models import Profile


class ProfileForm(BootstrapFormMixin, forms.ModelForm):
   
    class Meta:
        model = Profile
        exclude = ('user', 'is_complete')
