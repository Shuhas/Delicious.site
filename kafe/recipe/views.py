from django.shortcuts import render
from .models import *

# Create your views here.
def index(requests):
    return render(requests, 'index.html', {})


def about(requests):
    return render(requests, 'about.html', {})


def contact(requests):
    root = Suggestion()
    if requests.POST:
        root.name = requests.POST.get('name')
        root.email = requests.POST.get('email')
        root.subject = requests.POST.get('subject')
        root.message = requests.POST.get('message')
        root.save()
    return render(requests, 'contact.html', {})


def receipe(requests):
    return render(requests, 'receipe-post.html', {})



