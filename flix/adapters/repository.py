import abc
from flix.domain.model import *

repository_instance = None


class RepositoryException(Exception):

    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add_user(self, user: User):
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, username) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def add_movie(self, movie: Movie):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie(self, movie) -> Movie:
        raise NotImplementedError

    @abc.abstractmethod
    def add_actor(self, actor: Actor):
        raise NotImplementedError

    @abc.abstractmethod
    def get_actors(self, actor) -> Actor:
        raise NotImplementedError

    @abc.abstractmethod
    def add_genre(self, genre: Genre):
        raise NotImplementedError

    @abc.abstractmethod
    def get_genres(self, genre) -> Genre:
        raise NotImplementedError

    @abc.abstractmethod
    def add_director(self, director: Director):
        raise NotImplementedError

    @abc.abstractmethod
    def get_director(self, director) -> Director:
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_actor(self, actor: Actor):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_director(self, director: Director):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_genre(self, genre: Genre):
        raise NotImplementedError

    @abc.abstractmethod
    def get_number_of_movies(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_id(self, movie_ids):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_year(self, year: int):
        raise NotImplementedError

