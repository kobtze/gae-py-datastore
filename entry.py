from google.cloud import datastore
import datetime

KIND = 'Entry'
client = datastore.Client(project='fs-py-datastore')


def get_entry(name):
    key = client.key(KIND, name)
    entry = client.get(key)
    return entry


def set_entry(name, value):
    complete_key = client.key(KIND, name)
    # TODO: add reverse mechanism
    # 0. call get
    # 1. if current name exists => add set_backwards obj {name, value} to Commands
    # 2. else => add unset
    entry = datastore.Entity(key=complete_key)
    entry.update({'value': value})
    result = client.put(entry)
    return result


def unset_entry(name):
    # TODO: add reverse mechanism
    # 0: call get
    # 1. if exists => add set_backwards
    # 2. else => add set_backwards(null)
    complete_key = client.key(KIND, name)
    result = client.delete(complete_key)
    return result


def num_equal_to(value):
    query = client.query(kind=KIND)
    query.keys_only()
    query.add_filter('value', '=', value)
    results = list(query.fetch())
    num = (len(results))
    return num


def clean():
    # Query entire DB
    query = client.query()
    query.keys_only()
    # Fetch
    entries = list(query.fetch())
    # Only case where time complexity is O(n)
    result = client.delete_multi(entries)
    return result
