import pytest
from src.controllers.usercontroller import UserController
#from src.util.dao import DAO

import unittest.mock as mock

@pytest.fixture
def user_controller_returns_user():
    #user_controller = UserController(DAO)
    mocked_dao = mock.MagicMock()
    mocked_dao.find.return_value = [{ "_id": "66229e5e49cd7ea5bde165e2", "email": "axel.oj@outlook.com", "firstName": "Axel", "lastName": "Jönsson" }]
    user_controller_returns_user = UserController(mocked_dao)
    return user_controller_returns_user


@pytest.fixture
def existing_email():
    existing_email = "axel.oj@outlook.com"
    return existing_email

@pytest.fixture
def existing_user_obj():
    existing_user_obj = { "_id": "66229e5e49cd7ea5bde165e2", "email": "axel.oj@outlook.com", "firstName": "Axel", "lastName": "Jönsson" }
    return existing_user_obj

@pytest.fixture
def invalid_email():
    invalid_email = "asd123_moas.com"
    return invalid_email




@pytest.mark.unit
def test_get_user_by_email_one_user(user_controller_returns_user, existing_email, existing_user_obj):
    result = user_controller_returns_user.get_user_by_email(existing_email)
    assert result == existing_user_obj








"""
    @pytest.mark.unit
    def test_get_user_by_email_invalid_email_format(user_controller, invalid_email):
        result = UserController.get_user_by_email(user_controller, invalid_email)
        assert result == ValueError
"""