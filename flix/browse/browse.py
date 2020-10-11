from flask import Blueprint, render_template, url_for, request

import flix.utilities.utilities as utilities
import flix.adapters.repository as repo
from flix import Actor, Genre, Director

browse_blueprint = Blueprint('browse_bp', __name__)


@browse_blueprint.route('/browse_by_year', methods=['GET'])
def browse_by_year():
    target_year = request.args.get('year')
    if target_year is None:
        target_year = 2011
    else:
        target_year = int(target_year)
    first_year = url_for('browse_bp.browse_by_year', year=2006)
    last_year = url_for('browse_bp.browse_by_year', year=2016)
    if target_year == 2006:
        previous_year = None
        first_year = None
    else:
        previous_year = url_for('browse_bp.browse_by_year', year=target_year - 1)
    if target_year == 2016:
        next_year = None
        last_year = None
    else:
        next_year = url_for('browse_bp.browse_by_year', year=target_year + 1)

    return render_template(
        'browse/browse.html',
        movies=utilities.get_movies_by_year(target_year),
        previous=previous_year,
        next=next_year,
        current=target_year,
        first=first_year,
        last=last_year
    )


@browse_blueprint.route('/browse_by_actors', methods=['GET'])
def browse_by_actors():
    actor_list = utilities.get_actors()
    actor = request.args.get('actor')
    page = request.args.get('page')
    if actor is None:
        actor = actor_list[992]
    else:
        actor = Actor(actor)
    if page is None:
        page = 992
    elif int(page) < 0:
        page = 0
    else:
        page = int(page)
    first_actor = url_for('browse_bp.browse_by_actors', actor=actor_list[0].actor_full_name, page=0)
    last_actor = url_for('browse_bp.browse_by_actors', actor=actor_list[1984].actor_full_name, page=1984)
    if actor == actor_list[0]:
        previous_actor = None
        first_actor = None
    else:
        previous_actor = url_for('browse_bp.browse_by_actors', actor=actor_list[page-1].actor_full_name, page=page-1)
    if actor == actor_list[1984]:
        next_actor = None
        last_actor = None
    else:
        next_actor = url_for('browse_bp.browse_by_actors', actor=actor_list[page+1].actor_full_name, page=page+1)
    return render_template(
        'browse/browse.html',
        movies=utilities.get_movies_by_actor(actor),
        previous=previous_actor,
        next=next_actor,
        current=actor.actor_full_name,
        first=first_actor,
        last=last_actor

    )


@browse_blueprint.route('/browse_by_genres', methods=['GET'])
def browse_by_genres():
    genre_list = utilities.get_genres()
    genre = request.args.get('genre')
    page = request.args.get('page')
    if genre is None:
        genre = genre_list[9]
    else:
        genre = Genre(genre)
    if page is None:
        page = 9
    elif int(page) < 0:
        page = 0
    else:
        page = int(page)
    first_genre = url_for('browse_bp.browse_by_genres', genre=genre_list[0].genre_name, page=0)
    last_genre = url_for('browse_bp.browse_by_genres', genre=genre_list[19].genre_name, page=19)
    if genre == genre_list[0]:
        previous_genre = None
        first_genre = None
    else:
        previous_genre = url_for('browse_bp.browse_by_genres', genre=genre_list[page-1].genre_name, page=page-1)
    if genre == genre_list[19]:
        next_genre = None
        last_genre = None
    else:
        next_genre = url_for('browse_bp.browse_by_genres', genre=genre_list[page+1].genre_name, page=page+1)
    return render_template(
        'browse/browse.html',
        movies=utilities.get_movies_by_genre(genre),
        previous=previous_genre,
        next=next_genre,
        current=genre.genre_name,
        first=first_genre,
        last=last_genre
    )


@browse_blueprint.route('/browse_by_directors', methods=['GET'])
def browse_by_directors():
    director_list = utilities.get_directors()
    director = request.args.get('director')
    page = request.args.get('page')
    if director is None:
        director = director_list[321]
    else:
        director = Director(director)
    if page is None:
        page = 321
    elif int(page) < 0:
        page = 0
    else:
        page = int(page)
    first_director = url_for('browse_bp.browse_by_directors', director=director_list[0].director_full_name, page=0)
    last_director = url_for('browse_bp.browse_by_directors', director=director_list[643].director_full_name, page=643)
    if director == director_list[0]:
        previous_director = None
        first_director = None
    else:
        previous_director = url_for('browse_bp.browse_by_directors', director=director_list[page-1].director_full_name, page=page-1)
    if director == director_list[643]:
        next_director = None
        last_director = None
    else:
        next_director = url_for('browse_bp.browse_by_directors', director=director_list[page+1].director_full_name, page=page+1)
    return render_template(
        'browse/browse.html',
        movies=utilities.get_movies_by_director(director),
        previous=previous_director,
        next=next_director,
        current=director.director_full_name,
        first=first_director,
        last=last_director

    )