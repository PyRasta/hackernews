from django.db.models import fields
from .models import CreateAccount, FindAccount
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

class FindForm(ModelForm):
    class Meta:
        model = FindAccount
        fields = ["username",'password']   
        widgets = {
            "username": TextInput(attrs={
                "class":'pole',
            }),
            'password': TextInput(attrs={
                "type": "password",
            })
        }