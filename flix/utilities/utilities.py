from flask import Blueprint, request, render_template, redirect, url_for, session

import flix.adapters.repository as repo
import flix.utilities.services as services

utilities_blueprint = Blueprint('utilities', __name__)


def get_random_movie(quantity=10):
    movie = services.get_random_movie(quantity, repo.repo_instance)
    return movie


def get_movies_by_year(year):
    movies = services.get_movies_by_year(year, repo.repo_instance)
    return movies


def get_actors():
    actors = services.get_actors(repo.repo_instance)
    return actors


def get_movies_by_actor(actor):
    movies = services.get_movies_by_actor(actor, repo.repo_instance)
    return movies


def get_genres():
    genres = services.get_genres(repo.repo_instance)
    return genres


def get_movies_by_genre(genre):
    movies = services.get_movies_by_genre(genre, repo.repo_instance)
    return movies


def get_directors():
    directors = services.get_directors(repo.repo_instance)
    return directors


def get_movies_by_director(director):
    movies = services.get_movies_by_director(director, repo.repo_instance)
    return movies
