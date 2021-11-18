from django.shortcuts import HttpResponse
from project_1.models import Film


def film_delete(request, film_id):
    try:
        film = Film.objects.get(id=film_id)
    except Film.DoesNotExist:
        return HttpResponse('Failed')
    film.delete(id=film_id)
    return HttpResponse('Sucessful')


def home(request):
    film = Film.objects.all()
    return HttpResponse('Hi Python')


film_2 = Film(name='Forrest Gump', rate=5, is_published=True, status=1)
film_2.save()


def films(request):
    try:
        film = Film.objects.get(id=1)
    except Film.DoesNotExist:
        film = None
        film = Film.objects.filter(rate=5)
        print(film.query)
        return HttpResponse(film)
