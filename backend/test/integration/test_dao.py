import pytest
from pymongo import MongoClient 
from src.util.dao import DAO

from unittest.mock import patch

from src.util.dao import DAO

@patch('src.util.dao.getValidator', autospec=True)
@pytest.fixture
<<<<<<< HEAD
def mongodb():
    """
    Sets up a in-memory database. Cleans up the database efter yield.
    """
    # Create a in-memory MongoDB and crete database 'dbtest'
    client = MongoClient('mongodb://localhost:27017/dbtest')
    yield client
    # Cleans up the database 'dbtest'
    client.drop_db('dbtest')

@pytest.fixture
def data_access_object(mongodb):
    """
    Creates an instance of DAO, pointing to the test database.
    """
    # Connect to the database 
    db = mongodb['dbtest']
    # Create an instance of DAO 
    dao = DAO(db)
    return dao

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
    assert created_document['is_active'] == True
=======
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
>>>>>>> 6c126dc7dface910d9c7e9b92695de5fee29f034
