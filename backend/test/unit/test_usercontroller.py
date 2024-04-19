
import pytest
from src.controllers.usercontroller import UserController
#from src.util.dao import DAO

import unittest
import unittest.mock as mock

""" 
    Eftersom vi mockar dao.find return value så behöver vi inte matcha det mot databasens faktiska innehåll, vi kan alltså själva hitta på.
"""

@pytest.fixture
def user_controller_returns_user():
    mocked_dao = mock.MagicMock()
    mocked_dao.find.return_value = [{ "_id": "ABC123", "email": "axel.oj@outlook.com", "firstName": "Axel", "lastName": "Jönsson" }]
    user_controller_returns_user = UserController(mocked_dao)
    return user_controller_returns_user




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

