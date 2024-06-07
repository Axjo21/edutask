import pytest
import pymongo
import os
from dotenv import dotenv_values
from src.util.dao import DAO

@pytest.fixture(scope="module")
def test_dao():
    # Läs in miljövariabler från .env-filen
    LOCAL_MONGO_URL = dotenv_values('.env').get('MONGO_URL')
    
    # Kontrollera om det finns en MONGO_URL i miljövariablerna och använd den om den finns, annars använd LOCAL_MONGO_URL
    MONGO_URL = os.environ.get('MONGO_URL', LOCAL_MONGO_URL)
    
    # Anslut till MongoDB och välj den relevanta databasen
    print(f'Connecting to MongoDB at URL: {MONGO_URL}')
    client = pymongo.MongoClient(MONGO_URL)
    database = client.edutask
    
    # Skapa en instans av DAO för teständamål och returnera den
    test_dao = DAO("test_collection")
    yield test_dao

    # Efter att testerna har körts, rensa databasen genom att ta bort alla dokument från test_collection
    test_dao.collection.delete_many({})
    
    # Stäng anslutningen till databasen efter att testerna har körts
    client.close()

@pytest.mark.integration
def test_something_with_database(test_dao):
    # Förbered testmiljön genom att infoga några testdata i databasen
    test_data = [
        {"name": "John", "age": 30},
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 35}
    ]
    test_dao.collection.insert_many(test_data)

    # Utför operationen du vill testa, t.ex. räkna antalet dokument i databasen
    result = test_dao.collection.count_documents({})

    # Verifiera resultatet av operationen genom att jämföra det med förväntat resultat
    expected_length = len(test_data)
    print(f"Actual result: {result}, Expected result: {expected_length}")
    assert result == expected_length


