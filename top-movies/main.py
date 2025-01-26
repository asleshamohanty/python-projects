from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = ''
Bootstrap5(app)

movie_api_key=""
#url = "https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1"
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2NjNmNDMwNjhiMGQxYmFhYjIxOTZjNTcyZGZmOTkyNCIsInN1YiI6IjY2NDU3ZjFjZjYwM2I5ZDNhNzhkN2Y0NyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.flaxQba7BaWnDStJjM0nrek4dhXzTv_XSD_mvtz0qiM"
}

# CREATE DB
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
# Create the extension
db = SQLAlchemy(model_class=Base)
# initialise the app with the extension
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    image_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()

# ## After adding the new_movie the code needs to be commented out/deleted.
# ## So you are not trying to add the same movie twice. The db will reject non-unique movie titles.
# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     image_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )
#
# with app.app_context():
#     db.session.add(second_movie)
#     db.session.commit()

class RateMovieForm(FlaskForm):
    rating = StringField(label='Your Rating out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField(label='Your Review', validators=[DataRequired(), Length(min=1, max=75)])
    submit = SubmitField(label='Done')

class AddMovieForm(FlaskForm):
    name = StringField(label='Movie Name', validators=[DataRequired()])
    submit = SubmitField(label='Done')


@app.route("/")
def home():
    # # READ ALL RECORDS
    # # Construct a query to select from the database. Returns the rows in the database
    # result = db.session.execute(db.select(Movie).order_by(Movie.title))
    # # Use .scalars() to get the elements rather than entire rows from the database
    # all_movies = result.scalars().all() #all converts it to a python list
    # for i in range(len(all_movies)):
    #     all_movies[i].ranking = len(all_movies) - i
    # db.session.commit()
    movie_list = Movie.query.order_by(Movie.rating).all()
    for movie in movie_list[::-1]:
        movie.ranking = len(movie_list) - movie_list.index(movie)
        db.session.commit()
    return render_template("index.html", all_movies=movie_list)

@app.route("/update", methods=["GET", "POST"])
def update():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        try:
            movie.rating = float(form.rating.data)
        except ValueError:
            movie.rating = movie.rating
        finally:
            movie.review = form.review.data
            db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))




@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_title=form.name.data
        response = requests.get(url=MOVIE_DB_SEARCH_URL, params={"api_key":movie_api_key, "query":movie_title})
        data=response.json()["results"]
        return render_template("select.html", options=data)

    return render_template("add.html", form=form)


@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        response = requests.get(movie_api_url, params={"api_key": movie_api_key, "language": "en-US"})
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            rating=0,
            ranking=0,
            review=" ",
            image_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"])
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('update', id=new_movie.id))




if __name__ == '__main__':
    app.run(debug=True)
