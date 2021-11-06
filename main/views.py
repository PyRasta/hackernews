from django.shortcuts import render, redirect
from .models import Article, CreateAccount, FindAccount
from .forms import CreateForm, FindForm
import time

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip    

def get_user_id():
    online_bd = FindAccount.objects.order_by("-id")[:1]
    for el in online_bd:
        return el.id

def check_online(request):
    flag = bool
    username = ""
    online = FindAccount.objects.all()
    user_ip = get_client_ip(request)
    for el in online:
        if user_ip == el.ip:
            flag = True
            username = el.username
            break        
        else:
            flag = False
    check = {
        "username": username,
        "flag": flag
    }        
    return check

def delete_online(request):
    username = ''
    user_ip = get_client_ip(request)
    online = FindAccount.objects.all()
    for el in online:
        if user_ip == el.ip:
            username = el.username    
            break
        else:
            return redirect('home')
    user_delete = FindAccount.objects.get(username = username)  
    user_delete.delete()  
    return redirect('home')

def update_bd(request):
    user_ip = get_client_ip(request)
    user_id = get_user_id()
    user = FindAccount.objects.get(id = user_id)
    user.ip = user_ip
    user.save()

def index(request):
    check = check_online(request)
    articls = Article.objects.order_by("id")[:30]   
    contex = {
        'articls': articls,
        'check': check,
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
                    update_bd(request)
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
    global login 
    login = contex
    return render(request, 'main/reg_log.html', contex)    

def new(request, login):
    return render(request, 'main/new.html', login)

def past(request, login):
    return render(request, 'main/past.html', login)

def comments(request , login):
    return render(request, 'main/comments.html', login)

def ask(request , login):
    return render(request, 'main/ask.html', login)

def show(request , login):
    return render(request, 'main/show.html', login)

def jobs(request , login):
    return render(request, 'main/jobs.html', login)

def submit(request , login):
    return render(request, 'main/submit.html', login)

def welcome(request):
    return render(request, "main/welcome.html",)

def guidelines(request):
    return render(request, "main/guidelines.html",)

def threads(request , login):
    return render(request, 'main/threads.html', login)