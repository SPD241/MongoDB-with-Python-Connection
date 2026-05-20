from pymongo import MongoClient
from bson import ObjectId

class MongoDBCRUD:

    #definimos constructor con parámetros de conexion con MongoDB
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["DataAirbnb"]
        self.collection = self.db["Data"]

    #crear documento con algunos parámetros de prueba
    def create_document(self, name: str, country: str, price: float):
        new_user = {
            "name": name,
            "country": country,
            "price": price
        }
        try: 
            result = self.collection.insert_one(new_user)
            print(f"Document inserted with ID: {result.inserted_id}")
        except Exception as e:
            print(f"An error occurred while inserting the document: {e}")

    #buscar documento por ID
    def read_document(self, id:str):
        id = ObjectId(id)
        for user in self.collection.find({"_id": id}):
            print(f"Name: {user['name']}, Country: {user['country']}, Price: {user['price']}")

    #actualizar documento
    def update_document(self, id:str, param: str, value):
        id = ObjectId(id)
        update_ = self.collection.update_one({"_id": id}, {"$set": {param: value}})
        print(f"Updated {update_.modified_count} document(s)")
    
    #eliminar documento
    def delete_document(self, id:str):
        id = ObjectId(id)
        delete_ = self.collection.delete_one({"_id": id})
        print(f"Deleted {delete_.deleted_count} document(s)")

if __name__ == "__main__":
    mongo_crud = MongoDBCRUD()
    #mongo_crud.create_document("John Doe", "USA", 100.0)
    #mongo_crud.read_document(id="6a0d0c22e5f9a18f93d9b35e")
    mongo_crud.update_document(id="6a0d015f1320ab6a2430d959", param="price", value=195)
    #mongo_crud.delete_document(id="6a0d0c22e5f9a18f93d9b35e")