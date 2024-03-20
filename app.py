from flask import Flask, redirect, render_template, request, url_for

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    return render_template('list_all_movies.html', list_movies_active=True)


@app.route('/movies/new', methods=['GET', 'POST'])
def create_movies_form():
    if request.method == 'POST':
        # Modified: Handle form submission for creating a new movie
        movie_name = request.form.get('movie_name')
        director = request.form.get('director')
        rating = int(request.form.get('rating'))

        #Modified: Save the movie with rating to the database using movie_repository
        movie_repository.create_movie(movie_name, director, rating)

        #Modified: After creating the movie in the database, redirect to the list all movies page
        return redirect(url_for('list_all_movies', 
                                movie_name=movie_name, 
                                director=director, 
                                rating=rating))

    # If it's a GET request, render the form to create a new movie rating.
    return render_template('create_movies_form.html', create_rating_active=True)
 


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    movie_name = request.form.get('movie_name')
    director = request.form.get('director')
    rating = int(request.form.get('rating'))

    movie_repository.create_movie(movie_name, director, rating)

    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)


@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    # TODO: Feature 4
    return render_template('get_single_movie.html')


@app.get('/movies/<int:movie_id>/edit')
def get_edit_movies_page(movie_id: int):
    return render_template('edit_movies_form.html')


@app.post('/movies/<int:movie_id>')
def update_movie(movie_id: int):
    # TODO: Feature 5
    # After updating the movie in the database, we redirect back to that single movie page
    return redirect(f'/movies/{movie_id}')


@app.post('/movies/<int:movie_id>/delete')
def delete_movie(movie_id: int):
    # TODO: Feature 6
    pass