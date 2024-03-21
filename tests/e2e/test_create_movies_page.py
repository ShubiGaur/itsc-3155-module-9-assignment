import pytest
from flask.testing import FlaskClient
from app import app, movie_repository # Ensure you're importing your Flask app instance and the movie_repository

@pytest.fixture
def test_app():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_movie(test_app: FlaskClient):
    # Clear the database to ensure a clean state
    movie_repository.clear_db()

    # Test creating a movie with valid inputs
    response = test_app.post('/movies', data={
        'title': "Schindler's List",
        'director': 'Steven Spielberg',
        'rating': '5'
    })
    assert response.status_code == 302 # Assuming a redirect after successful creation

    # Verify the movie was created
    movies = movie_repository.get_all_movies()
    assert len(movies) == 1

    # Access the first (and only) movie in the dictionary
    movie = next(iter(movies.values()))
    assert movie.title == "Schindler's List"
    assert movie.director == 'Steven Spielberg'
    assert movie.rating == 5
