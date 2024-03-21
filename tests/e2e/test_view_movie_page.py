# TODO: Feature 4
import pytest
from src.repositories.movie_repository import get_movie_repository


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

def test_view_movie_page(client, app):
    # Create a test movie
    test_movie = Movie(title="Test Movie", director="Test Director", rating=5)
    db.session.add(test_movie)
    db.session.commit()

    # Test accessing the movie page
    response = client.get(f'/movies/{test_movie.id}')
    assert response.status_code == 200
    assert b"Test Movie" in response.data
    assert b"Test Director" in response.data
    assert b"5" in response.data
