import re

from pymongo import MongoClient
import pymongo

def test_get_database_and_collection():
        with MongoClient("172.17.0.2", 27017) as client:
            test_db = client.test_db
            book_collection = test_db.book_collection

            assert book_collection is not None

def test_document_insert_and_find_one():
        with MongoClient("172.17.0.2", 27017) as client:
            test_db = client.test_db
            book_collection = test_db.book_collection

            book = {"isbn": "978-4873117386", "title": "入門 Python 3", "price": 4070}

            book_collection.insert_one(book)

            assert book_collection.find_one({"isbn": "978-4873117386"})["title"] == book["title"]
            assert book_collection.count_documents({}) == 1

            book_collection.delete_many({})
            assert book_collection.count_documents({}) == 0
