from django.urls import path
from .views import *
from .recipes import views as rec_views

urlpatterns = [
    path('', index, name='dashboard-home'),
    path('rec/list/', rec_views.rec_list, name='rec-list')
]