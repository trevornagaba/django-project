from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    # display all polls questions

    return HttpResponse('Hello polls')
