
import pytest
from src.controllers.usercontroller import UserController
#from src.util.dao import DAO

import unittest
import unittest.mock as mock
from unittest.mock import patch

""" 
    Eftersom vi mockar dao.find return value så behöver vi inte matcha det mot databasens faktiska innehåll, vi kan alltså själva hitta på.
    Detta testar däremot inte funktionaliteten för att faktiskt hämta rätt anv från databasen, men det är en annan del av koden så det testar vi inte här.
"""

@pytest.fixture
def user_controller_returns_user():
    mocked_dao = mock.MagicMock()
    mocked_dao.find.return_value = [{ "_id": "ABC123", "email": "axel.oj@outlook.com", "firstName": "Axel", "lastName": "Jönsson" }]
    user_controller_returns_user = UserController(mocked_dao)
    return user_controller_returns_user


@pytest.fixture
def user_controller_returns_first_user():
    mocked_dao = mock.MagicMock()
    mocked_dao.find.return_value = [
        { "_id": "ABC123", "email": "axel.oj@outlook.com", "firstName": "Axel", "lastName": "Jönsson" },
        { "_id": "XIIV", "email": "axel.oj@outlook.com", "firstName": "anskfl", "lastName": "asdlkn" },
        { "_id": "MXVI", "email": "axel.oj@outlook.com", "firstName": "asdl", "lastName": "asdlkn" },
        { "_id": "XVII", "email": "axel.oj@outlook.com", "firstName": "skdal", "lastName": "aslkn" }
        ]
    user_controller_returns_user = UserController(mocked_dao)
    return user_controller_returns_user

@pytest.fixture
def user_controller_returns_none():
    mocked_dao = mock.MagicMock()
    mocked_dao.find.return_value = None
    user_controller_returns_none = UserController(mocked_dao)
    return user_controller_returns_none

@pytest.fixture
def user_controller_returns_exception():
    mocked_dao = mock.MagicMock()
    mocked_dao.find.return_value = Exception
    user_controller_returns_exception = UserController(mocked_dao)
    return user_controller_returns_exception


@pytest.mark.unit
def test_get_user_by_email_one_user(user_controller_returns_user):
    """ Tests that correct user gets returned when passing a valid and existing email """
    result = user_controller_returns_user.get_user_by_email("axel.oj@outlook.com")
    assert result == { "_id": "ABC123", "email": "axel.oj@outlook.com", "firstName": "Axel", "lastName": "Jönsson" }


@pytest.mark.unit
def test_get_user_by_email_invalid_email_format(user_controller_returns_user):
    """ Tests that ValueError gets raised when passing email with invalid format """
    with pytest.raises(ValueError):
        user_controller_returns_user.get_user_by_email("invalid__email.com")



@pytest.mark.unit
def test_get_user_by_email_first_user(user_controller_returns_first_user):
    """ Tests that the first user gets returned when passing a valid and existing email when multiple ones exist """
    result = user_controller_returns_first_user.get_user_by_email("viktor@gmail.se")
    assert result == { "_id": "ABC123", "email": "axel.oj@outlook.com", "firstName": "Axel", "lastName": "Jönsson" }


@pytest.mark.unit
def test_get_user_by_email_exception(user_controller_returns_exception):
    """ Tests that Exception gets raised when database encounters failure """
    with pytest.raises(TypeError):
        user_controller_returns_exception.get_user_by_email("axel.oj@outlook.com")


#@pytest.mark.unit
def test_get_user_by_email_none(user_controller_returns_none):
    """ Tests that None gets returned when passing a valid email """
    result = user_controller_returns_none.get_user_by_email("axel.oj@outlook.com")
    assert result == None
