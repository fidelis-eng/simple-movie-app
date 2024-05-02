from .handler.movie_handler import get_popular_movies_handler, get_movie_handler,json_to_database_handler, get_movies_by_name_handler

def search_by_name(request):
    return get_movies_by_name_handler(request)

def detail(request, movie_id):  
    return get_movie_handler(request, movie_id)
def home(request):
    return get_popular_movies_handler(request)

# add dummy data from json file
def json_to_database(request): 
    return json_to_database_handler(request)