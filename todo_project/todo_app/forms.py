from django.forms import Form, CharField, TextInput, HiddenInput


class TodoForm(Form):
    title = CharField(required=True)
    description = CharField(required=True)
    owner = CharField(required=True)
    bot_catcher = CharField(
        widget=HiddenInput,
        required=False,
    )


