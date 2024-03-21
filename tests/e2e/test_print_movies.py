# Import necessary modules
from src.repositories.movie_repository import get_movie_repository

# Define the test function
def test_print_movies():
    # Get the movie repository
    movie_repo = get_movie_repository()
    
    # Get all movies from the repository
    movies = movie_repo.get_all_movies()
    
    # Print out the details of each movie
    for movie in movies.values():
        print(f"Movie ID: {movie.movie_id}")
        print(f"Title: {movie.title}")
        print(f"Director: {movie.director}")
        print(f"Rating: {movie.rating}")
        print("--------------")

# Run the test function
test_print_movies()
