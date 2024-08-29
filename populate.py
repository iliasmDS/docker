from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from numpy.random import randint
import pandas as pd

database_name = 'mongodb'
collection_name = 'data'

def collect_data():

    """
    Some data generation process
    """

    df = pd.DataFrame()

    for i in range(1, 101):

        df.loc[i, 'x'] = randint(1,101)

        df.loc[i, 'y'] = randint(1,101)

    return df.to_dict('records')

def initialize_db():
        
    client = MongoClient(

                        host='container_as_db',
                        port=27017, 
                        username='root', 
                        password='pass',
                        authSource="admin"
                            
                        )
        
    db = client[database_name]
        
    collection = db[collection_name]

    data = collect_data()

    collection.insert_many(data)
        
    client.close()

if __name__ == "__main__":
    
    initialize_db()