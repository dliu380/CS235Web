from datetime import date

import pytest

from flix.authentication.services import AuthenticationException
from flix.authentication import services as auth_services


def test_can_add_user(in_memory_repo):
    new_username = 'jz'
    new_password = 'abcd1A23'

    auth_services.add_user(new_username, new_password, in_memory_repo)

    user_as_dict = auth_services.get_user(new_username, in_memory_repo)
    assert user_as_dict['username'] == new_username

    # Check that password has been encrypted.
    assert user_as_dict['password'].startswith('pbkdf2:sha256:')


def test_cannot_add_user_with_existing_name(in_memory_repo):
    username = 'thorke'
    password = 'abcd1A23'

    with pytest.raises(auth_services.NameNotUniqueException):
        auth_services.add_user(username, password, in_memory_repo)


def test_authentication_with_invalid_credentials(in_memory_repo):
    new_username = 'pmccartney'
    new_password = 'abcd1A23'

    auth_services.add_user(new_username, new_password, in_memory_repo)

    with pytest.raises(auth_services.AuthenticationException):
        auth_services.authenticate_user(new_username, '0987654321', in_memory_repo)