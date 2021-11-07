from django.db.models import fields
from django.http.response import FileResponse
from .models import CreateAccount, FindAccount, CheckPost
from django.forms import ModelForm, TextInput, Textarea, widgets


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
            }),
        }
class ArticleForm(ModelForm):
    class Meta:
        model = CheckPost
        fields = ["title", "url"]
        widgets = {
            "title": TextInput(attrs={
                "type": "text"
            }),
            "url": TextInput(attrs={
                "type": 'text',
                "class": 'input_two',
            }),
        }