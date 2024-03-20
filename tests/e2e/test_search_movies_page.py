import pytest
from app import app

@pytest.fixture
def test_client():
    """Create a test client for the Flask app."""
    with app.test_client() as client:
        yield client

def test_search_existing_movie(test_client):
    """Test searching for an existing movie."""
    # Send a GET request to search for the movie "Avatar"
    response = test_client.get('/movies/search?search=Avatar')

    # Check if the response status code is 200 OK
    assert response.status_code == 200

    # Check if the response contains the expected movie details
    assert b'Avatar' in response.data
    assert b'James Cameron' in response.data
    assert b'7' in response.data  # Assuming the rating is 7

def test_search_nonexistent_movie(test_client):
    """Test searching for a nonexistent movie."""
    # Send a GET request to search for a nonexistent movie
    response = test_client.get('/movies/search?search=Nonexistent')

    # Check if the response status code is 200 OK
    assert response.status_code == 200

    # Check if the response contains a message indicating that the movie was not found
    assert b'No Movie Found' in response.data

if __name__ == "__main__":
    pytest.main()