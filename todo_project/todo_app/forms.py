from django.core.validators import EmailValidator
from django.forms import Form, CharField, TextInput, HiddenInput, Textarea, ValidationError, IntegerField, NumberInput, \
    EmailField, EmailInput, PasswordInput
import re


def check_for_name(value):
    if not value[0].isupper():
        raise ValidationError('The name must start with an uppercase letter.')


def check_for_age(value):
    if value < 0:
        raise ValidationError('The age cannot be less than zero.')


def check_for_pass(value):
    if not re.fullmatch(r'([a-zA-Z0-9]).{7,}$', value):
        raise ValidationError("Enter a valid password.")


def clean_bot_catcher(value):
    if value:
        raise ValidationError('This form was created by a bot')


class TodoForm(Form):
    title = CharField(max_length=20, validators=[check_for_name])
    description = CharField(widget=Textarea)
    owner = CharField(max_length=100)


class FormName(Form):
    name = CharField(validators=[check_for_name])
    age = IntegerField(widget=NumberInput, validators=[check_for_age])
    email = EmailField(widget=EmailInput, validators=[EmailValidator])
    password = CharField(widget=PasswordInput, validators=[check_for_pass])
    text = CharField(widget=Textarea)
    bot_catcher = CharField(required=False, widget=HiddenInput, max_length=0, validators=[clean_bot_catcher])
