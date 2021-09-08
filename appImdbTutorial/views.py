from appImdbTutorial.forms import FilmForm
from django.shortcuts import redirect, render, get_object_or_404
from .models import Film
from .forms import FilmForm
from django.contrib.auth.decorators import login_required

# Create your views here.
# from django.http import HttpResponse
# def text_response(request) :
#     return HttpResponse('<h1>First test</h1>')

def all_movies(request) :
    all_movies = Film.objects.all()
    test = 'Variable inside all_movies method'
    return render(request, 'films.html', {'film': all_movies, 'text': test})

@login_required
def new_movie(request) :
    if_new = True
    form = FilmForm(request.POST or None, request.FILES or None)

    if form.is_valid() :
        form.save()
        return redirect(all_movies)

    return render(request, 'movie_form.html', {'form': form, 'isNew': if_new})

@login_required
def edit_movie(request, id) :
    if_new = False
    movie = get_object_or_404(Film, pk=id) # no primary key in our model
    form = FilmForm(request.POST or None, request.FILES or None, instance=movie)

    if form.is_valid() :
        form.save()
        return redirect(all_movies)

    return render(request, 'movie_form.html', {'form': form, 'isNew': if_new})

@login_required
def delete_movie(request, id) :
    movie = get_object_or_404(Film, pk=id) # no primary key in our model
    
    if request.method == 'POST' :
        movie.delete()
        return redirect(all_movies)

    return render(request, 'confirm.html', {'film': movie})