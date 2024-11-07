from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    return HttpResponse('Hello World from views.py!!!')

def say_HELLO(request):
    return render(request, 'hello.html', {'name': 'Shadab'})
