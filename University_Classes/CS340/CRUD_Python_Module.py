# Example Python Code to Insert a Document 

from typing import Any, Dict, List, Optional
from pymongo import MongoClient
from pymongo.errors import PyMongoError

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(
        self,
        username: str,
        password: str,
        host: str = "localhost",
        port: int = 27017,
        db_name: str = "aac",
        collection_name: str = "animals",
    ):
        """ Initialize MongoDB connection using authentication.

        Args:
            username: MongoDB username ('aacuser')
            password: MongoDB password
            host: MongoDB host (default: localhost)
            port: MongoDB port (default: 27017)
            db_name: Database name (default: aac)
            collection_name: Collection name (default: animals)
        """
        try:
            uri = f"mongodb://{username}:{password}@{host}:{port}"
            self.client = MongoClient(uri)
            self.database = self.client[db_name]
            self.collection = self.database[collection_name]
        except PyMongoError as exc:                # Fail fast with a clear error if the DB connection is broken
            raise RuntimeError(f"Failed to connect to MongoDB: {exc}") from exc

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data: Optional[Dict[str, Any]]) -> bool:
        if not data or not isinstance(data, dict):
            return False

        try:
            result = self.collection.insert_one(data)
            return result.acknowledged
        except PyMongoError:
            return False

    # Create method to implement the R in CRUD.
    # This method uses find() and returns the results as a list, else return an empty list.
    def read(self, query: Optional[Dict[str, Any]]) -> List[Dict[str, Any]]:
        if query is None or not isinstance(query, dict):
            return []

        try:
            cursor = self.collection.find(query)
            return list(cursor)
        except PyMongoError:
            return []
        
    # Create method to implement the U in CRUD.
    
    def update(self, query: Optional[Dict[str, Any]], new_values: Optional[Dict[str, Any]]) -> int:
        if query is None or not isinstance(query, dict):
            return 0
        if new_values is None or not isinstance(new_values, dict) or len(new_values) == 0:
            return 0

        try:
            # Use update_many to match the rubric language ("document(s)")
            result = self.collection.update_many(query, {"$set": new_values})
            return result.modified_count
        except PyMongoError:
            return 0

    # Create method to implement the D in CRUD.
    
    def delete(self, query: Optional[Dict[str, Any]]) -> int:
        if query is None or not isinstance(query, dict):
            return 0

        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except PyMongoError:
            return 0