from datetime import date

from flix.domain.model import User, Actor, Genre, Director, Movie, Review

import pytest


@pytest.fixture()
def actor():
    return Actor('50 Cent')


@pytest.fixture()
def user():
    return User('dbowie', '1234567890')


@pytest.fixture()
def genre():
    return Genre('Action')


@pytest.fixture()
def director():
    return Director('Taika Waititi')


@pytest.fixture()
def movie():
    return Movie('Kimi no na wa', 2016)


def test_user_construction(user):
    assert user.user_name == 'dbowie'
    assert user.password == '1234567890'
    assert repr(user) == '<User dbowie>'


def test_actor_construction(actor):
    assert actor.actor_full_name == '50 Cent'
    assert repr(actor) == '<Actor 50 Cent>'
    assert actor < Actor('Adam Sandler')
    actor.add_actor_colleague(Actor('Adam Sandler'))
    assert actor.check_if_this_actor_worked_with(Actor('Adam Sandler')) == True


def test_genre_construction(genre):
    assert genre.genre_name == 'Action'
    assert repr(genre) == '<Genre Action>'
    assert genre < Genre('Horror')


def test_director_construction(director):
    assert director.director_full_name == 'Taika Waititi'
    assert repr(director) == '<Director Taika Waititi>'
    assert director < Director('Tom Ford')


def test_movie_construction(movie):
    assert movie.title == 'Kimi no na wa'
    assert movie.release_year == 2016