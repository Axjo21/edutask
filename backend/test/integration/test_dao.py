import pytest
from pymongo import MongoClient 
from src.util.dao import DAO

from unittest.mock import patch

from src.util.dao import DAO

@patch('src.util.dao.getValidator', autospec=True)
@pytest.fixture
def mongodb():
    """
    Sets up a in-memory database. Cleans up the database efter yield.
    """
    # Create a in-memory MongoDB and crete database 'dbtest'
    mongodb = MongoClient('mongodb://localhost:27017/dbtest')
    yield mongodb
    # Cleans up the database 'dbtest'
    mongodb.drop_db('dbtest')

@pytest.fixture
def data_access_object(mongodb):
    """
    Creates an instance of DAO, pointing to the test database.
    """
    # Connect to the database 
    db = mongodb['dbtest']
    # Create an instance of DAO 
    dao = DAO("_db__testing_")
    return dao

@pytest.mark.integration
def test_create_document(data_access_object):
    # Define test data
    test_data = {
        'name': 'Test Document',
        'is_active': True
    }

    # Call the create method of your data access object
    created_document = data_access_object.create(test_data)

    # Assert that the created document contains the expected data
    assert created_document['name'] == 'Test Document'
    #assert created_document['is_active'] == True
