import pytest
from flask import url_for
from src.repositories.movie_repository import get_movie_repository
from app import app # Import from app.py


# telling flask the the server name, application root, and preferred URL scheme to correctly build URLs
# aka just e2e testing stuff that pytests needs to be able to run according to the internet

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SERVER_NAME'] = 'localhost' # The server name
    app.config['APPLICATION_ROOT'] = '/' # The application root
    app.config['PREFERRED_URL_SCHEME'] = 'http' # The preferred URL scheme
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_all_movies_page(client):
    # Clear the database so that the movie DB is empty when you boot it up
    movie_repository = get_movie_repository()
    movie_repository.clear_db()

    # Add some test movies
    test_movies = [
        {'title': 'Morbius', 'director': 'Daniel Espinosa', 'rating': 10},
        {'title': 'Inception', 'director': 'Christopher Nolan', 'rating': 8},
        {'title': 'The Shawshank Redemption', 'director': 'Frank Darabont', 'rating': 9}
    ]
    for movie_data in test_movies:
        movie_repository.create_movie(movie_data['title'], movie_data['director'], movie_data['rating'])

    # Visit the all movies page
    response = client.get(url_for('list_all_movies'))

    # Make sure the response status code is 200 (OK)
    assert response.status_code == 200

    # Make sure the page contains the titles of the test movies
    for movie in test_movies:
        assert movie['title'] in response.data.decode()
