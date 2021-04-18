import os
from pymongo import MongoClient

COLLECTION_NAME = 'inventory'


class MongoRepository(object):
    def __init__(self):
        mongo_url = os.environ.get('MONGO_URL')
        self.db = MongoClient(mongo_url).db

    def find_all(self, selector):
        return self.db.inventory.find(selector)

    def find(self, selector):
        return self.db.inventory.find_one(selector)

    def create(self, item):
        return self.db.inventory.insert_one(item)

    def update(self, selector, item):
        return self.db.inventory.replace_one(selector, item).modified_count

    def delete(self, selector):
        return self.db.inventory.delete_one(selector).deleted_count
