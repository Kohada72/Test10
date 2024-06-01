from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

#uri = "mongodb+srv://al22005:pOSrTuopGEEhSU6E@cluster0.16pm7pd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
#client = MongoClient(uri)


from pymongo import MongoClient
def get_database():

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    uri = "mongodb+srv://al22005:pOSrTuopGEEhSU6E@cluster0.16pm7pd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(uri)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['user_shopping_list']

# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
    # Get the database
    dbname = get_database()
    