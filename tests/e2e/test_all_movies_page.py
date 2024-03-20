# TODO: Feature 1
from app import movie_repository
from flask.testing import FlaskClient
def test_list_all_movies(test_app: FlaskClient):
    movie_repository.create_movie('Morbius', 'Daniel Espinosa', 10.0)
    response = test_app.get('/movies')
    assert b'Morbius' in response.data