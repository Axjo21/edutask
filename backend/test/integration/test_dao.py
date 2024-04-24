import pytest
import pymongo
import re

from unittest.mock import patch, MagicMock
from src.util.dao import DAO


@pytest.fixture
#@patch('src.util.dao.pymongo.MongoClient')
def sut():
    """ Create a test database and """
    #mongo_client.return_value.edutask = pymongo.MongoClient('mongodb://localhost:27017/dbtest')
    mocked_dao = DAO(collection_name='test_collection')

    yield mocked_dao

    mocked_dao.drop()




@pytest.mark.integration
def test_dao_create_obj(sut):
    """ Test that create method works as intended with a validated object """

    data = {'name': 'axel', 'security': '1234123', 'email': 'aoj@mail.com'}
    created_object = sut.create(data)
    o_id = created_object['_id']

    assert created_object == {'_id':  o_id, **data}

