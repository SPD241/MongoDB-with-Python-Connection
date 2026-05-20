from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

class MongoDBConnection:

    #Definimos el constructor de la clase donde declaro parámetros para MongoDB
    def __init__(self):
        self.mongo_URI = "mongodb://localhost:27017/"
        self.Timeout = 5000

    #bloque de conexión para trazabilidad del error
    def connection(self):
        try:
            client = MongoClient(self.mongo_URI, serverSelectionTimeoutMS=self.Timeout)

            client.admin.command('ping')
            print("Connected to MongoDB successfully!")

            print("MongoDB Info:")
            for db_name in client.list_database_names():
                print(f" - {db_name}")
        
        except ConnectionFailure:
            print(f"Failed to connect to MongoDB")
        except Exception as e:
            print(f"An error occurred: {e}")

