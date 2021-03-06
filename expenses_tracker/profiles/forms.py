from django import forms

from profiles.models import Profile


class ProfileForm(forms.ModelForm):

    class Meta:

        model = Profile
        fields = ('budget', 'first_name', 'last_name')
