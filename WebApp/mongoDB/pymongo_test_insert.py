# Get the database using the method we defined in pymongo_test_insert file
from pymongo_get_database import get_database
#from dateutil import parser
dbname = get_database()
collection_name = dbname["users"]

item_1 = {
    "_id" : "U1IT00001",
    "item_name" : "Blender",
    "max_discount" : "10%",
    "batch_number" : "RR450020FRG",
    "price" : 340,
    "category" : "kitchen appliance"
}

item_2 = {
    "_id" : "U1IT00002",
    "item_name" : "Egg",
    "category" : "food",
    "quantity" : 12,
    "price" : 36,
    "item_description" : "brown country eggs"
}
'''
existing_ids = [item['_id'] for item in collection_name.find({}, {'_id': 1})]  # Get all existing _id values from the collection
new_items = [item for item in [item_1, item_2] if item['_id'] not in existing_ids]  # Filter out items with duplicate _id
if new_items:
    collection_name.insert_many(new_items)
else:
    print("No new items to insert, all _id values already exist.")
'''


user_with_ingredients1 = {
        "_id": 4,
        "username": "user1",
        "ingredients": [
            {
                #本来は"name" : "food_name",
                "name": "tomato",
                "num": 5,
            },
            {
                "name": "flour",
                "num": 2,
            },
            {
                "name": "milk",
                "num": 1,
            }
        ]
    }
user_with_ingredients2 = {
        "_id": 3,
        "username": "user3",
        "ingredients": [
            {
                #本来は"name" : "food_name",
                "name": "orange",
                "num": 10,
            },
            {
                "name": "flour",
                "num": 2,
            },
            {
                "name": "milk",
                "num": 1,
            }
        ]
    }
collection_name.insert_many([user_with_ingredients1, user_with_ingredients2])

#collection_name.insert_many([item_1,item_2])
'''
expiry_date = '2021-07-13T00:00:00.000Z'
expiry = parser.parse(expiry_date)
item_3 = {
    "item_name" : "Bread",
    "quantity" : 2,
    "ingredients" : "all-purpose flour",
    "expiry_date" : expiry
}
collection_name.insert_one(item_3)
'''
