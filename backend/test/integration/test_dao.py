import pytest

from unittest.mock import patch

from src.util.dao import DAO

@patch('src.util.dao.getValidator', autospec=True)
@pytest.fixture
def sut():
    
    mocked_dao = DAO("new_test_collection")

    yield mocked_dao

    # create DAO
    # mock hard-coded dependencies?

    # setup collection
    # setup validator

    # setup done -> start testing create method

    # yield

    # tear down / cleanup collection
