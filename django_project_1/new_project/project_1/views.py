from django.shortcuts import HttpResponse
from project_1.models import Film

#
film_s = Film.objects.get(id=1)
film_s.delete()


def home(request):
    film = Film.objects.all()
    return HttpResponse('Hi Python')

#
film_2 = Film(name='Harry Potter', rate=6, is_published=True, status=2)
film_2.save()


def films(request):
    try:
        film = Film.objects.get(id=1)
    except Film.DoesNotExist:
        film = None
        film = Film.objects.filter(rate=5)
        print(film.query)
        return HttpResponse(film)
