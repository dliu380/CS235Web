"""Initialize Flask app."""

import os

from flask import Flask
import flix.adapters.repository as repo
from flix.adapters.memory_repository import *


def create_app(test_config=None):

    app = Flask(__name__)

    app.config.from_object('config.Config')
    data_path = os.path.join('flix', 'adapters', 'data')

    if test_config is not None:
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']

    repo.repo_instance = MemoryRepository()
    movies = MovieFileCSVReader(os.path.join(data_path, 'Data1000Movies.csv'))
    movies.read_csv_file()
    for movie in movies.dataset_of_movies:
        repo.repo_instance.add_movie(movie)
    for actor in sorted(movies.dataset_of_actors):
        repo.repo_instance.add_actor(actor)
    for genre in sorted(movies.dataset_of_genres):
        repo.repo_instance.add_genre(genre)
    for director in sorted(movies.dataset_of_directors):
        repo.repo_instance.add_director(director)
    load_users(data_path, repo.repo_instance)

    with app.app_context():
        from .home import home
        app.register_blueprint(home.home_blueprint)
        from .browse import browse
        app.register_blueprint(browse.browse_blueprint)
        from .authentication import authentication
        app.register_blueprint(authentication.authentication_blueprint)
    return app
