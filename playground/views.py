import re
from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return render(request, 'hello.html', {'name': 'ali'})
