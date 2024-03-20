# test_all_movies_page.py

# Import necessary modules
from app import movie_repository
from flask.testing import FlaskClient

# Define the test case
def test_list_all_movies(test_app: FlaskClient):
    # Create fake movies in the repository
    movie_repository.create_movie('Fake Movie 1', 'Fake Director 1', 8.5)
    movie_repository.create_movie('Fake Movie 2', 'Fake Director 2', 7.0)
    movie_repository.create_movie('Fake Movie 3', 'Fake Director 3', 6.5)

    # Test listing all movies
    response = test_app.get('/movies')
    assert b'Fake Movie 1' in response.data
    assert b'Fake Movie 2' in response.data
    assert b'Fake Movie 3' in response.data
