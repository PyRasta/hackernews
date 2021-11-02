from django.shortcuts import render, redirect
from .models import Article, CreateAccount, FindAccount
from .forms import CreateForm, FindForm
import time



def index(request):
    articls = Article.objects.order_by("id")[:30]
    online = FindAccount.objects.all()
    contex = {
        'articls': articls,
        'online': online
    }
    return render(request, 'main/index.html', contex)

def logreg(request):
    find_error = ''
    create_error = ''
    base = CreateAccount.objects.all()
    create_form = CreateForm(request.POST)
    find_form = FindForm(request.POST)
    if request.method == "POST":
        if request.POST.get('name'):
            name = request.POST['name']
            for el in base:
                if el.name == name:
                    create_error = "Этот пользователь уже есть!!"
                    break 
            if create_error == "":
                create_form.save()         

        if request.POST.get('username'):
            username = request.POST['username']
            password = request.POST["password"]
            for el in base:
                if username == el.name:
                    find_error = True
                    passwd = el.password
                    break
            if find_error == True:
                if password == passwd:
                    find_form.save()
                    find_error = "Вы авторизовались"
                    return redirect("home")
                else:
                    find_error = "Неверный пароль" 
    
            if find_error == '':
                find_error = "Неправильно введено имя пользователя"         

    create_form = CreateForm()
    find_form = FindForm()
    contex = {
        'find_form': find_form,
        'create_form': create_form,
        'create_error': create_error,
        'find_error': find_error
    }
    return render(request, 'main/reg_log.html', contex)    

def new(request):
    return render(request, 'main/new.html')

def past(request):
    return render(request, 'main/past.html')

def comments(request):
    return render(request, 'main/comments.html')

def ask(request):
    return render(request, 'main/ask.html')

def show(request):
    return render(request, 'main/show.html')

def jobs(request):
    return render(request, 'main/jobs.html')

def submit(request):
    return render(request, 'main/submit.html')
                       