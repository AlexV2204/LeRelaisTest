from django.shortcuts import render
from django.http import HttpResponse


def index(resquest):
    return HttpResponse("Hello, world, You're at the article index.")
