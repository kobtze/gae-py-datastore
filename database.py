from google.cloud import datastore
from flask import jsonify

client = datastore.Client(project='fs-py-datastore')


class Database:

    def get(self, kind, name):
        key = client.key(kind, name)
        entry = client.get(key)
        return entry

    def set(self, kind, name, value):
        key = client.key(kind, name)
        entry = datastore.Entity(key)
        # print(entry)
        res = entry.update({'value': value})
        # print(res)
        result = client.put(entry)
        return result

    def query_by_value(self, kind, value):
        query = client.query(kind=kind)
        query.keys_only()
        query.add_filter('value', '=', value)
        return list(query.fetch())

    def delete_one(self, kind, name):
        key = client.key(kind, name)
        result = client.delete(key)
        # print(result)
        return result

    def clean(self):
        query = client.query()
        # query.keys_only()
        entries = list(query.fetch())
        # Only case where time complexity is O(n)
        result = client.delete_multi(entries)
        return result
