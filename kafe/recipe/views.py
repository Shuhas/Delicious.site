from django.shortcuts import render


# Create your views here.
def index(requests):
    return render(requests, 'index.html', {})


def about(requests):
    return render(requests, 'about.html', {})


def contact(requests):
    return render(requests, 'contact.html', {})


def receipe(requests):
    return render(requests, 'receipe-post.html', {})

