import pytest
from src.controllers.usercontroller import UserController
from src.util.dao import DAO


@pytest.fixture
def user_controller():
    user_controller = UserController(DAO)

@pytest.fixture
def existing_email():
    existing_email = "axel.oj@outlook.com"

@pytest.fixture
def existing_user_obj():
    existing_user_obj = { "_id": "66229e5e49cd7ea5bde165e2", "email": "axel.oj@outlook.com", "firstName": "Axel", "lastName": "Jönsson" }

@pytest.fixture
def invalid_email():
    invalid_email = "asd123_moas.com"

@pytest.mark.unit
def test_get_user_by_email_one_user(user_controller, existing_email, existing_user_obj):
    result = UserController.get_user_by_email(user_controller, existing_email)
    assert result == existing_user_obj


@pytest.mark.unit
def test_get_user_by_email_invalid_email_format(user_controller, invalid_email):
    result = UserController.get_user_by_email(user_controller, invalid_email)
    assert result == ValueError
