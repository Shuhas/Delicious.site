from django.urls import path
from .views import about, index, contact, receipe

urlpatterns = [
    path("", index, name='index'),
    path("about/", about, name='about'),
    path("contact/", contact, name='contact'),
    path("receipe", receipe, name='receipe'),
]

