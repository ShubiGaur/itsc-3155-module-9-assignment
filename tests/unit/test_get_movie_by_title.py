# test_movie_repository.py

import pytest
from src.repositories.movie_repository import get_movie_repository

@pytest.fixture
def temp_movie_repository():
    # Creating a movie repository
    return get_movie_repository()

def setup_module(module):
    # Adding movies to the movie repository
    temp_movie_repository = get_movie_repository()
    temp_movie_repository.create_movie('Movie A', 'Director A', 1)
    temp_movie_repository.create_movie('Movie B', 'Director B', 2)
    temp_movie_repository.create_movie('Movie C', 'Director C', 3)
    temp_movie_repository.create_movie('Movie D', 'Director D', 4)

def test_get_existing_movie_by_title(temp_movie_repository):
    # Testing if you can get an existing movie by its title
    movie_test_1 = temp_movie_repository.get_movie_by_title('Movie A')
    assert movie_test_1.title == 'Movie A'

    movie_test_2 = temp_movie_repository.get_movie_by_title('Movie B')
    assert movie_test_2.title == 'Movie B'

    movie_test_3 = temp_movie_repository.get_movie_by_title('Movie C')
    assert movie_test_3.title == 'Movie C'

    movie_test_4 = temp_movie_repository.get_movie_by_title('Movie D')
    assert movie_test_4.title == 'Movie D'

def test_get_nonexisting_movie_by_title(temp_movie_repository):
    # Testing if you get None when trying to get a non-existing movie by its title
    non_existing_movie = temp_movie_repository.get_movie_by_title('Nonexisting Movie')
    assert non_existing_movie is None


