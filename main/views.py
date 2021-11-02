from django.shortcuts import render, redirect
from .models import Article, CreateAccount
from .forms import CreateForm

def index(request):
    articls = Article.objects.order_by("id")[:30]
    return render(request, 'main/index.html', {'articls': articls})

def logreg(request):
    flag = True
    error = ''
    base = CreateAccount.objects.all()
    form = CreateForm(request.POST)
    if request.method == "POST":
        username = request.POST['name']
        for el in base:
            if el.name == username:
                error = "Этот пользователь уже есть!!"
                break 
        if error == "":
            form.save()        
    form = CreateForm()
    contex = {
        'form': form,
        'error': error
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
                       