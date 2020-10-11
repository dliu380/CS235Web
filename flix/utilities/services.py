import random

from flix.adapters.repository import AbstractRepository
from flix.domain.model import *


def get_random_movie(quantity, repo: AbstractRepository):
    movie_count = repo.get_number_of_movies()
    random_ids = random.sample(range(1, movie_count), quantity)
    movies = repo.get_movie_by_id(random_ids)
    return movies


def get_movies_by_year(year, repo: AbstractRepository):
    movies = repo.get_movie_by_year(year)
    return movies


def get_actors(repo: AbstractRepository):
    actors = repo.get_actors()
    return actors


def get_movies_by_actor(actor, repo: AbstractRepository):
    movies = repo.get_movie_by_actor(actor)
    return movies


def get_genres(repo: AbstractRepository):
    genres = repo.get_genres()
    return genres


def get_movies_by_genre(genre, repo: AbstractRepository):
    movies = repo.get_movie_by_genre(genre)
    return movies


def get_directors(repo: AbstractRepository):
    directors = repo.get_director()
    return directors


def get_movies_by_director(director, repo: AbstractRepository):
    movies = repo.get_movie_by_director(director)
    return movies
