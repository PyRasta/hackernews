from django.shortcuts import render
from .models import Article

def index(request):
    articls = Article.objects.order_by("id")[:30]
    return render(request, 'main/index.html', {'articls': articls})

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
                       