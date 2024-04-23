import pytest

from unittest.mock import patch

from src.util.dao import DAO

#class TestMyClass(unittest.TestCase):

@patch('src.util.dao.getValidator', autospec=True)
@pytest.fixture
def sut():
    mocked_dao = DAO("new_test_collection")

    yield mocked_dao

    mocked_dao.drop()




@pytest.mark.integration
def test_dao_create(sut):
    """ Tests that dao.create method works as intended """
    result = sut.create({ "_id": "ABC123", "email": "axel.oj@outlook.com", "firstName": "Axel", "lastName": "Jönsson" })
    assert result == { "_id": "ABC123", "email": "axel.oj@outlook.com", "firstName": "Axel", "lastName": "Jönsson" }


