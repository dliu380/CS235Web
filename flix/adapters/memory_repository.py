import csv
import os

from werkzeug.security import generate_password_hash

from flix.adapters.repository import AbstractRepository
from flix.domain.model import *


class MemoryRepository(AbstractRepository):

    def __init__(self):
        self._movies = []
        self._actors = []
        self._genres = []
        self._directors = []
        self._users = []

    def add_user(self, user: User):
        self._users.append(user)

    def get_user(self, username) -> User:
        return next((user for user in self._users if user.user_name == username), None)

    def add_movie(self, movie: Movie):
        self._movies.append(movie)

    def get_movie(self, movie) -> Movie:
        return self._movies

    def add_actor(self, actor: Actor):
        self._actors.append(actor)

    def get_actors(self):
        return self._actors

    def add_genre(self, genre: Genre):
        self._genres.append(genre)

    def get_genres(self):
        return self._genres

    def add_director(self, director: Director):
        self._directors.append(director)

    def get_director(self):
        return self._directors

    def get_movie_by_actor(self, actor: Actor):
        movie_list = []
        for movie in self._movies:
            if actor in movie.actors:
                movie_list.append(movie)
        return movie_list

    def get_movie_by_director(self, director: Director):
        movie_list = []
        for movie in self._movies:
            if director == movie.director:
                movie_list.append(movie)
        return movie_list

    def get_movie_by_genre(self, genre: Genre):
        movie_list = []
        for movie in self._movies:
            if genre in movie.genres:
                movie_list.append(movie)
        return movie_list

    def get_number_of_movies(self):
        return len(self._movies)

    def get_movie_by_id(self, movie_ids):
        movies = [self._movies[id] for id in movie_ids]
        return movies

    def get_movie_by_year(self, year: int):
        movie_list = []
        for movie in self._movies:
            if movie.release_year == year:
                movie_list.append(movie)
        return movie_list


class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__dataset_of_movies = []
        self.__dataset_of_actors = set()
        self.__dataset_of_directors = set()
        self.__dataset_of_genres = set()

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            for row in movie_file_reader:
                movie = Movie(row['Title'], int(row['Year']))
                movie.description = row['Description']
                movie.runtime_minutes = int(row['Runtime (Minutes)'])

                director = Director(row['Director'])
                self.__dataset_of_directors.add(director)
                movie.director = director

                parsed_genres = row['Genre'].split(',')
                for genre_string in parsed_genres:
                    genre = Genre(genre_string)
                    self.__dataset_of_genres.add(genre)
                    movie.add_genre(genre)

                parsed_actors = row['Actors'].split(',')
                for actor_string in parsed_actors:
                    actor = Actor(actor_string)
                    self.__dataset_of_actors.add(actor)
                    movie.add_actor(actor)

                self.__dataset_of_movies.append(movie)

    @property
    def dataset_of_movies(self) -> list:
        return self.__dataset_of_movies

    @property
    def dataset_of_actors(self) -> set:
        return self.__dataset_of_actors

    @property
    def dataset_of_directors(self) -> set:
        return self.__dataset_of_directors

    @property
    def dataset_of_genres(self) -> set:
        return self.__dataset_of_genres


def read_csv_file(filename: str):
    with open(filename, encoding='utf-8-sig') as infile:
        reader = csv.reader(infile)

        # Read first line of the the CSV file.
        headers = next(reader)

        # Read remaining rows from the CSV file.
        for row in reader:
            # Strip any leading/trailing white space from data read.
            row = [item.strip() for item in row]
            yield row


def load_users(data_path: str, repo: MemoryRepository):
    users = dict()

    for data_row in read_csv_file(os.path.join(data_path, 'users.csv')):
        user = User(
            user_name=data_row[1],
            password=generate_password_hash(data_row[2])
        )
        repo.add_user(user)
        users[data_row[0]] = user
    return users
