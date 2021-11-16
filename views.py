from django.shortcuts import HttpResponse

from to_do.models import Film

# from to_do.models import Task

film_d = Film.objects.get(id=1)
film_d.delete()

film_2 = Film(name='Harry Potter', rate=5, is_punlished=True, status=2)
film_2.save()


def home_1(request):
    films = Film.objects.all()

    return HttpResponse('hello there {} {}'.format(films[1], films[2]))


def film(request):
    film_4 = Film(name='Home Alone', rate=5, is_punlished=True, status=2)
    film_4.save()
    films = Film.objects.all()
    return HttpResponse('Hello python {} {} {}'.format(films[0], films[1], films[2]))


def help_film(request):
    try:
        films = Film.objects.get(id=1, name='Forrest Gump', rate=9)
    except Film.DoesNotExist:
        films = None
        films = Film.objects.filter(name='Home alone', rate=5)
        print(films.query)
        return HttpResponse(films)

