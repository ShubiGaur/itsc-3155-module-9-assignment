# TODO: Feature 4
import pytest
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:' # Use an in-memory database for testing
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

def test_get_movie_by_id(app):
    # Create a test movie
    test_movie = Movie(title="Test Movie", director="Test Director", rating=5)
    db.session.add(test_movie)
    db.session.commit()

    # Initialize the repository with the test app's database
    movie_repository = MovieRepository(db)

    # Test fetching the movie by ID
    fetched_movie = movie_repository.get_movie_by_id(test_movie.id)
    assert fetched_movie is not None
    assert fetched_movie.title == "Test Movie"
    assert fetched_movie.director == "Test Director"
    assert fetched_movie.rating == 5
