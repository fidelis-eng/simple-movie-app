from django.shortcuts import render
import json
from django.http import HttpResponse, HttpResponseNotFound
from ..models import Movie, Genre
from ..model_response.responses import MovieResponse

# get all movies from database
def get_all_movies_handler(request):
    movies = Movie.objects.all()
    context = {"movies": movies}
    return render(request, 'home.html', context)

# get one movie and the details
def get_movie_handler(request, movie_id):
    try:
        movie_detail = Movie.objects.get(pk=movie_id)  
        # movie object 
        movie_obj = MovieResponse(
            id= movie_detail.id, 
            name= movie_detail.name, 
            description= movie_detail.description,
            img_path= movie_detail.img_path,
            duration= movie_detail.duration,
            genre= [genre.genre_name for genre in movie_detail.genres.all()],
            language= movie_detail.language,
            mpaa_rating_type=movie_detail.mpaa_rating_type,
            mpaa_rating_label= movie_detail.mpaa_rating_label,
            user_rating= str(movie_detail.user_rating)
        )
        context = {"movie_info": movie_obj}
        return render(request, 'detail.html', context)
    except:
        print("Movie not found")
        return render(request, '404_page.html')

# add data (json file) to database
def json_to_database_handler(request):
    movies_json = "./movies.json"
    with open(movies_json) as json_file:
        data = json.load(json_file)       
        for d in data:
            genres = d['genre'] # genre from current movie
            for genre in genres:
                try:
                    new_genre = Genre(genre_name=genre)
                    new_genre.save()
                except:
                    continue
            # add data
            m = Movie(
                name=d['name'],
                description=d['description'],
                img_path=d['imgPath'],
                duration=d['duration'],
                language=d['language'],
                mpaa_rating_type=d['mpaaRating']['type'],
                mpaa_rating_label=d['mpaaRating']['label'],
                user_rating=d['userRating']
                )
            m.save()
            # add genre to movie
            for g in genres:
                g = Genre.objects.get(genre_name=g)
                m.genres.add(g)

        print(Movie.objects.all())
        print()
        print(Genre.objects.all())

    return HttpResponse('successfully add dummy data')

