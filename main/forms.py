from .models import CreateAccount
from django.forms import ModelForm, TextInput, widgets


class CreateForm(ModelForm):
    class Meta:
        model = CreateAccount
        fields = ['name', 'password']
        widgets = {
            'name': TextInput(attrs={
                "class": "pole",
            }),
            'password': TextInput(attrs={
                'type': "password",
            })

        }