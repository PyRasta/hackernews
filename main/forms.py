from django.db.models import fields
from django.http.response import FileResponse
from .models import CreateAccount, FindAccount, Article
from django.forms import ModelForm, TextInput, HiddenInput, widgets


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
class PostArticle(ModelForm):
    class Meta:
        model = Article
        fields = ["title", "url"]
        widgets = {
            
        }