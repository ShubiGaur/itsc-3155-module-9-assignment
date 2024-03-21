# Feature 4
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository

def test_get_movie_by_id():
    movie_repository = get_movie_repository()
    movie = Movie(74523, 'Test Movie', 'Test Director', 5)
    movie_repository._db.update({movie.movie_id:movie})

    assert movie_repository.get_movie_by_id(74523) == movie