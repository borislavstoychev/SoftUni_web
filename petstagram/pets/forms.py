from django import forms

from pets.models import Pet


# class PetCreateForm(forms.ModelForm):
    # DOG = 'dog'
    # CAT = 'cat'
    # PARROT = 'parrot'
    # UNKNOWN = 'unknown'
    # PET_TYPE = (
    #     (DOG, "Dog"),
    #     (CAT, 'Cat'),
    #     (PARROT, 'Parrot'),
    #     (UNKNOWN, 'Unknown'),
    # )
    # type = forms.ChoiceField(choices=PET_TYPE, required=True, widget=forms.Select(
    #     attrs={
    #         'class': 'form-control'
    #     }
    # ))
    # name = forms.ChoiceField(required=True, widget=forms.TextInput(
    #     attrs={
    #         'class': 'form-control'
    #     }
    # ))
    # age = forms.IntegerField(required=True, widget=forms.TextInput(
    #     attrs={
    #         'class': 'form-control'
    #     }
    # ))
    #
    # description = forms.ChoiceField(required=True, widget=forms.Textarea(
    #     attrs={
    #         'class': 'form-control'
    #     }
    # ))
    #
    # image_url = forms.URLField(required=True, widget=forms.TextInput(
    #     attrs={
    #         'class': 'form-control'
    #     }
    # ))
class PetCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Pet
        fields = "__all__"