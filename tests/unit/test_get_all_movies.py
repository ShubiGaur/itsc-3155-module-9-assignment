# TODO: Feature 1
import pytest
from src.repositories.movie_repository import get_movie_repository

def test_get_all_movies():
    # Get the movie repository singleton
    movie_repository = get_movie_repository()

    # Clear the database to ensure a clean state
    movie_repository.clear_db()

    # Add some test movies
    test_movies = [
        {'title': 'Avatar', 'director': 'James Cameron', 'rating': 7},
        {'title': 'Inception', 'director': 'Christopher Nolan', 'rating': 8},
        {'title': 'The Shawshank Redemption', 'director': 'Frank Darabont', 'rating': 9}
    ]
    for movie_data in test_movies:
        movie_repository.create_movie(movie_data['title'], movie_data['director'], movie_data['rating'])

    # Retrieve all movies
    movies = movie_repository.get_all_movies()

    # Assert that the number of movies retrieved matches the number of test movies added
    assert len(movies) == len(test_movies)

    # Assert that the movies retrieved match the test movies
    for movie in movies.values():
        assert movie.title in [m['title'] for m in test_movies]
        assert movie.director in [m['director'] for m in test_movies]
        assert movie.rating in [m['rating'] for m in test_movies]
