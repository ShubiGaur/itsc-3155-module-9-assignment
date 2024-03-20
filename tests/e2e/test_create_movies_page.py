# TODO: Feature 2
import pytest
from src.repositories.movie_repository import get_movie_repository

@pytest.fixture
def movie_repo():
    """Fixture to provide a clean movie repository instance before each test."""
    movie_repository = get_movie_repository()
    movie_repository.clear_db()  # Clear the database before each test
    return movie_repository

def test_create_movie(movie_repo):
    """Test creating a movie rating."""
    # Arrange
    movie_name = "Test Movie"
    director = "Test Director"
    rating = 4

    # Act
    movie = movie_repo.create_movie(movie_name, director, rating)

    # Assert
    assert movie.id is not None
    assert movie.title == movie_name
    assert movie.director == director
    assert movie.rating == rating

def test_create_movie_bad_input(movie_repo):
    """Test creating a movie rating with bad input."""
    # Arrange
    movie_name = ""
    director = "Test Director"
    rating = 6  # Invalid rating

    # Act & Assert
    with pytest.raises(ValueError):
        movie_repo.create_movie(movie_name, director, rating)

def test_create_movie_duplicate_title(movie_repo):
    """Test creating a movie rating with a duplicate title."""
    # Arrange
    movie_name = "Duplicate Movie"
    director = "Test Director"
    rating = 3

    # Create the movie with the same title first
    movie_repo.create_movie(movie_name, director, rating)

    # Act & Assert
    with pytest.raises(ValueError):
        movie_repo.create_movie(movie_name, director, rating)

# You can add more tests for edge cases and other scenarios as needed

