from django.shortcuts import render
from .models import *


# Create your views here.
def index(requests):
    return render(requests, 'index.html', {})


def about(requests):
    return render(requests, 'about.html', {})


def contact(requests):
    root = [Suggestion(), Subscribes()]
    try:
        if requests.POST:
            root[0].name = requests.POST.get('name')
            root[0].email = requests.POST.get('email')
            root[0].subject = requests.POST.get('subject')
            root[0].message = requests.POST.get('message')
            root[0].save()
    except:
        if requests.POST:
            root[1].subs_email = requests.POST.get('subs_email')
    return render(requests, 'contact.html', {})


def receipe(requests, pk=1):
    post = Recipe.objects.all()
    ctgs = Category.objects.all()
    ctx = {
        'post': post,
        'ctgs': ctgs
    }
    return render(requests, 'receipe-post.html', {})
