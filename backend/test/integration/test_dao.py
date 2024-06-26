import pytest

from unittest.mock import patch
from src.util.dao import DAO


from unittest.mock import MagicMock
# Note: 
#       THIS SUITE ASSUMES THAT MONGODB IS UP AND RUNNING, THUS;
#       MONGODB NEEDS TO BE RUNNING LOCALLY FOR THE TESTS TO WORK AS INTENDED.
#       THE TESTS MAKE USE OF THE sut FIXTURE WHICH SETS UP A DAO WHICH WE WILL USE TO
#       PERFORM THE CREATE METHOD ON, AFTERWARDS WE CLEAN UP THE COLLECTION

@pytest.fixture
def json_structure():
    json_structure = {
            "$jsonSchema": {
                "bsonType": "object",
                "required": ["security", "email"],
                "properties": {
                    "name": {
                        "bsonType": "string",
                        "description": "the name of a user must be determined"
                    }, 
                    "security": {
                        "bsonType": "string",
                        "description": "the security nr of a user must be determined"
                    },
                    "email": {
                        "bsonType": "string",
                        "description": "the email address of a user must be determined",
                        "uniqueItems": True
                    }
                }
            }
        }
    return json_structure



@pytest.fixture
#@patch('src.util.dao.pymongo.MongoClient')
#@patch('src.util.dao.getValidator', autospec=True)
def sut():
    """ Create a test database and """
    #mongo_client.return_value.edutask = pymongo.MongoClient('mongodb://localhost:27017/dbtest')
    
    """validator = MagicMock()
    validator.return_value = {
            "$jsonSchema": {
                "bsonType": "object",
                "required": ["security", "email"],
                "properties": {
                    "name": {
                        "bsonType": "string",
                        "description": "the name of a user must be determined"
                    }, 
                    "security": {
                        "bsonType": "string",
                        "description": "the security nr of a user must be determined"
                    },
                    "email": {
                        "bsonType": "string",
                        "description": "the email address of a user must be determined",
                        "uniqueItems": True
                    }
                }
            }
        }
    print("VALIDATOR FROM FIXTURE: ", validator)
    """
    mocked_dao = DAO(collection_name='temp_tester')

    yield mocked_dao

    mocked_dao.drop()



#1
@pytest.mark.integration
def test_dao_create_obj(sut):
    """ Test that dao.create() works as intended with a validated object """
    data = {'name': 'axel', 'security': '1234123', 'email': 'aoj@mail.com'}
    created_object = sut.create(data)
    o_id = created_object['_id']

    assert created_object == {'_id':  o_id, **data}

#2
# THIS TEST DOESN'T PASS
# IT SHOULD RAISE EXCEPTION BECAUSE THE EMAIL ALREADY EXISTS IN ANOTHER DOCUMENT IN THE DATABASE
# AND THE EMAIL IS MARKED AS UNIQUE IN THE VALIDATOR
@pytest.mark.integration
def test_dao_create_field_not_unique(sut):
    """ Test that create method returns WriteError when field isn't unique among all documents"""

    data = {'name': 'axel', 'security': '1234123', 'email': 'aoj@mail.com'}
    sut.create(data)

    with pytest.raises(Exception):
        sut.create(data)

#3
@pytest.mark.integration
def test_dao_create_wrong_bson_type(sut):
    """ Test that dao.create() returns WriteError when wrong BSON type for field is passed """

    data = {'name': 1234, 'security': 'aoe', 'email': 'aom'}
    with pytest.raises(Exception):
        sut.create(data)


#4
@pytest.mark.integration
def test_dao_create_not_all_required_fields(sut):
    """ Test that dao.create() returns WriteError when all required fields aren't included"""

    data = {'name': 'axel', 'email': 'aoj@mail.com'}
    with pytest.raises(Exception):
        sut.create(data)

#5
@pytest.mark.integration
def test_dao_create_field_not_unique_and_not_all_fields_included(sut):
    """ Test that create method returns WriteError when field isn't unique and not included"""

    data = {'name': 'axel', 'security': '1234123', 'email': 'aoj@mail.com'}
    sut.create(data)

    with pytest.raises(Exception):
        sut.create({'name': 'axel', 'security': '1234123'})

#6
@pytest.mark.integration
def test_dao_create_wrong_bson_type_and_not_all_fields_included(sut):
    """ Test that dao.create() returns WriteError when wrong BSON type and not all required fields"""

    data = {'name': 1234, 'security': 'aoe'}
    with pytest.raises(Exception):
        sut.create(data)











# THE FOLLOWING TESTS WERE CREATED BUT DISCARDED SINCE THEY DID NOT ADHERE TO OUR INITIAL TEST DESIGN:

def test_dao_create_wrong_field(sut):
    """ Test that dao.create() returns WriteError wrong fields are passed"""

    data = {'name': 'axel', 'wrong_field_1': 'aoe', 'wrong_field_2': 'oiu'}
    with pytest.raises(Exception):
        sut.create(data)

def test_dao_create_empty(sut):
    """ Test that dao.create() returns WriteError when empty object is passed"""

    data = {}
    with pytest.raises(Exception):
        sut.create(data)

def test_dao_create_obj_no_name(sut):
    """ Test that dao.create() works as intended when no name is passed """

    data = {'security': '1234123', 'email': 'aoj@mail.com'}
    created_object = sut.create(data)
    o_id = created_object['_id']

    assert created_object == {'_id':  o_id, **data}
