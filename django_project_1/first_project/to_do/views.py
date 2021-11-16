from django.shortcuts import render, HttpResponse

# from to_do.models import Film

from to_do.models import Task

# film_2 = Film(name='Harry Potter', rate=5, is_punlished=True, status=2)
# film_2.save()


def home_1(request):
    # films = Film.objects.all()
    tasks = Task.objects.all()
    # return HttpResponse('hello there {} {}'.format(films[1], films[2]))
    return render(request, 'task/home.html')
#
# def film(request):
#     film_4 = Film(name='Home Alone', rate=5, is_punlished=True, status=2)
#     film_4.save()
#     films = Film.objects.all()
#     return HttpResponse('Hello python {} {} {}'.format(films[0], films[1], films[2]))
#
#
# def help_film(request):
#     try:
#         films = Film.objects.get(id=1, name='Forrest Gump', rate=9)
#     except Film.DoesNotExist:
#         films = None
#         films = Film.objects.filter(name='Home alone', rate=5)
#         print(films.query)
#         return HttpResponse(films)

# def home(request):
#     tasks = Task.objects.all()
#
#     return HttpResponse('hello there!! {} {} , Bye'.format(tasks[0], tasks[1]))
#
#
# def new_task(request):
#     new_1 = Task(title='three', description='test', status=2)
#     new_1.save()
#     tasks = Task.objects.all()
#     return HttpResponse('Hello Django {} {} {}'.format(tasks[5], tasks[4], tasks[3]))
#
#
# def filtered_data(request):
#     try:
#         task =Task.objects.get(id=1, title = 'New_one')
#     except Task.DoesNotExist:
#         task = None
#     # print(task.query)
#     task = Task.objects.filter(title='second')
#     return HttpResponse(task)
#
# # Create your views here.
# def home(request):
#     # print(request.__dict__)
#     return HttpResponse('Hello from Django app ')
#
#
# # def home_1(request):
# #     print(request.__dict__)
# #     return HttpResponse('Hello from Django app Aram')
#
# def present(request):
#
#     return HttpResponse("Aram Azatyan")
#
# def greeting(request):
#     return HttpResponse('Բարի գալուստ  Python Django - Welcome to Python Django')
#
# def introduction(request):
#
#     return HttpResponse('''Django (web framework)
#
#
#     Django is a Python-based free and open-source web framework that follows the model–template–views (MTV) architectural pattern.
#     It is maintained by the Django Software Foundation (DSF), an independent organization established in the US as a 501(c)(3) non-profit.
#     Django's primary goal is to ease the creation of complex, database-driven websites.
#     The framework emphasizes reusability and "pluggability" of components, less code, low coupling, rapid development, and the principle of don't repeat yourself.
#     Python is used throughout, even for settings, files, and data models.
#     Django also provides an optional administrative create, read, update and delete interface that is generated dynamically through introspection and configured via admin models.
#
#
#
#
#     ''')
#
# def time(request):
#     current_datetime = datetime.now()
#     return HttpResponse(f'current date and time - {current_datetime}')
#
# def solution_task(request):
#     a = [{x:x**2 for x in range(1,16)}]
#     return HttpResponse(a)
#
