""" this module inserts a new document in a collection based on kwargs"""
def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in the collection based on kwargs

    Args:
        mongo_collection: pymongo collection object
        **kwargs: key-value pairs representing the document

    Returns:
        The _id of the inserted document
    """
    return mongo_collection.insert_one(kwargs).inserted_id
