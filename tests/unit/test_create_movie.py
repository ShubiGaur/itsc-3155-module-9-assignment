# TODO: Feature 2
from src.models.movie import Movie

def test_create_movie():
    movie = Movie(1, 'The Incredibles', 'Brad Bird', 5)  

    assert movie
