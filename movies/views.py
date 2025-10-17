from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Movie
from .forms import MovieForm

def movie_list(request):
    # optional search by title
    q = request.GET.get('q', '').strip()
    movies = Movie.objects.all()
    if q:
        movies = movies.filter(MovieTitle__icontains=q)
    return render(request, 'movies/movie_list.html', {'movies': movies, 'q': q})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/movie_detail.html', {'movie': movie})

def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            messages.success(request, f"Added {movie}.")
            return redirect('movies:movie_detail', pk=movie.pk)
    else:
        form = MovieForm()
    return render(request, 'movies/movie_form.html', {'form': form, 'mode': 'Create'})

def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
            messages.success(request, f"Updated {movie}.")
            return redirect('movies:movie_detail', pk=movie.pk)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies/movie_form.html', {'form': form, 'mode': 'Update'})

def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        messages.info(request, "Movie deleted.")
        return redirect('movies:movie_list')
    return render(request, 'movies/movie_confirm_delete.html', {'movie': movie})
