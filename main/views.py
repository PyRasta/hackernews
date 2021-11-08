from django.http import request
from django.shortcuts import render, redirect
from .models import Article, CreateAccount, FindAccount, CheckPost
from .forms import CreateForm, FindForm, ArticleForm


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
    moder = bool
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
    for el in online:
        if el.moder:
            moder = True
            break
        else:
            moder = False
    check = {
        "username": username,
        "flag": flag,
        "moder": moder
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
    user_delete = FindAccount.objects.get(username=username)
    user_delete.delete()
    return redirect('home')


def update_bd(request):
    user_ip = get_client_ip(request)
    user_id = get_user_id()
    user = FindAccount.objects.get(id=user_id)
    username = user.username
    accounts = CreateAccount.objects.get(name=username)
    user.ip = user_ip
    user.moder = accounts.moder
    user.save()


def logreg(request):
    find_error = ''
    create_error = ''
    online = FindAccount.objects.all()
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
    return render(request, 'main/reg_log.html', contex)


def date_later():
    datetime = []
    articles = Article.objects.order_by("id")[:30]
    for el in articles:
        pass


def number_articles():
    articles = CheckPost.objects.all()
    number_articles = 0
    for el in articles:
        number_articles += 1
    return number_articles


def index(request):
    check = check_online(request)
    articles = Article.objects.order_by("id")
    number = number_articles()

    contex = {
        'articles': articles,
        'check': check,
        "number": number
    }
    return render(request, 'main/index.html', contex)


def new(request):
    check = check_online(request)
    contex = {
        'check': check,
    }
    return render(request, 'main/new.html', contex)


def past(request):
    check = check_online(request)
    contex = {
        'check': check,
    }
    return render(request, 'main/past.html', contex)


def comments(request):
    check = check_online(request)
    contex = {
        'check': check,
    }
    return render(request, 'main/comments.html', contex)


def ask(request):
    check = check_online(request)
    contex = {
        'check': check,
    }
    return render(request, 'main/ask.html', contex)


def show(request):
    check = check_online(request)
    contex = {
        'check': check,
    }
    return render(request, 'main/show.html', contex)


def jobs(request):
    check = check_online(request)
    contex = {
        'check': check,
    }
    return render(request, 'main/jobs.html', contex)


def get_post_id():
    bd_checkpost = CheckPost.objects.order_by("-id")[:1]
    for el in bd_checkpost:
        return el.id


def get_author(request):
    online = FindAccount.objects.all()
    user_ip = get_client_ip(request)
    for el in online:
        if user_ip == el.ip:
            username = el.username
            break
    return username


def update_post(request):
    id = get_post_id()
    post = CheckPost.objects.get(id=id)
    post.author = get_author(request)
    post.save()


def submit(request):
    error = ""
    if request.method == "POST":
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            update_post(request)
            return redirect("home")
        else:
            error = "Неверно введен url адрес"

    check = check_online(request)
    article_form = ArticleForm()
    contex = {
        'check': check,
        "article_form": article_form,
        "error": error
    }
    return render(request, 'main/submit.html', contex)


def welcome(request):
    return render(request, "main/welcome.html", )


def guidelines(request):
    return render(request, "main/guidelines.html", )


def threads(request):
    check = check_online(request)
    contex = {
        'check': check,
    }
    return render(request, 'main/threads.html', contex)
