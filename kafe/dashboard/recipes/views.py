from django.shortcuts import render

def rec_list(requst):
    return render(requst, 'dashboard/recipe/list.html')