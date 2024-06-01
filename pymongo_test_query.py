# Get the database using the method we defined in pymongo_test_insert file
from pymongo_get_database import get_database
from pandas import DataFrame

dbname = get_database()

# Retrieve a collection named "user_1_items" from database
collection_name = dbname["user_1_items"]

item_details = collection_name.find()
for item in item_details:
    # This does not give a very readable output
    #print(item['item_name'], item['category'])
    #output : Blender kitchen appliance
    #         Egg food
    print(item) 
    #output : {'_id': 'U1IT00001', 'item_name': 'Blender', 'max_discount': '10%', 'batch_number': 'RR450020FRG', 'price': 340, 'category': 'kitchen appliance'}
    #         {'_id': 'U1IT00002', 'item_name': 'Egg', 'category': 'food', 'quantity': 12, 'price': 36, 'item_description': 'brown country eggs'}
    
    # convert the dictionary objects to dataframe
    #items_df = DataFrame(item_details)

    # see the magic
    #print(items_df)
