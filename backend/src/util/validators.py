import json

validators = {}
def getValidator(collection_name: str):
    """Obtain a validator object of a collection which is stored as a json file with the same name. The validator must comply to a schema validation format (see https://www.mongodb.com/docs/manual/core/schema-validation/)

    parameters:
        collection_name -- the name of the collection, which should also be the filename

    returns:
        validator -- dict in the format of a MongoDB collection validator
    """
    # BEHÖVDE LÄGGA TILL EN TILL PUNKT HÄR FÖR ATT DET SKULLE FUNKA. BEHÖVDE INTE GÖRA DET FÖRUT DOCK?
    if collection_name not in validators:
        with open(f'../src/static/validators/{collection_name}.json', 'r') as f:
            validators[collection_name] = json.load(f)
    return validators[collection_name]