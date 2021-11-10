# from django.shortcuts import render
from django.shortcuts import HttpResponse
from datetime import datetime

# Create your views here.
def home(request):
    print(request.__dict__)
    return HttpResponse('Hello from Django app ')


# def home_1(request):
#     print(request.__dict__)
#     return HttpResponse('Hello from Django app Aram')

def present(request):

    return HttpResponse("Aram Azatyan")

def greeting(request):
    return HttpResponse('Welcome to Python Django')

def introduction(request):

    return HttpResponse('''Django (web framework)
    Django is a Python-based free and open-source web framework that follows the model–template–views (MTV) architectural pattern.
    It is maintained by the Django Software Foundation (DSF), an independent organization established in the US as a 501(c)(3) non-profit.
    Django's primary goal is to ease the creation of complex, database-driven websites. The framework emphasizes reusability and "pluggability" of components, less code, low coupling, rapid development, and the principle of don't repeat yourself.[9] Python is used throughout, even for settings, files, and data models. Django also provides an optional administrative create, read, update and delete interface that is generated dynamically through introspection and configured via admin models.
    ''')

def time(request):
    current_datetime = datetime.now()
    return HttpResponse(current_datetime)

def solution_task(request):
    a = [{x:x**2 for x in range(1,16)}]
    return HttpResponse(a)