from pymongo_get_database import get_database

dbname = get_database()

# Create a new collection

collection_name = dbname["user_1_items"]
#'_id'が'U1TT00001'
collection_name.update_one({'_id':'U1IT00001'}, {"$set": { 'price' : 350}})
