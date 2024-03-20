# TODO: Feature 1
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie
def test_list_all_movies():
    movie = Movie('Morbius', 'Daniel Espinosa', 10.0)

    assert type(movie) == Movie
    assert movie.title == 'Morbius'
    assert movie.director == 'Daniel Espinosa'
    assert movie.rating == 10.0