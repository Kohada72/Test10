from pymongo_get_database import get_database

dbname = get_database()

# Create a new collection
collection_name = dbname["user_1_items"]
collection_name.delete_one({'_id': 'U1IT00001'})
collection_name.delete_one({'_id': 'U1IT00002'})
#結果を閲覧
item_details = collection_name.find()
for item in item_details:
    # This does not give a very readable output
    #print(item['item_name'], item['category'])
    #output : Blender kitchen appliance
    #         Egg food
    print(item) 
