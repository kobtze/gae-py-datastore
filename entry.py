from database import Database
# import json

db = Database()

def get_entry(name):
    return db.get('Entry', name)

def set_entry(name, value):
    # Get previous val
    # prevalue = get_entry(name)
    db.set('Entry', name, value)
    # Insert command to done stack in DB:

def unset_entry(name):
    prev = db.get('Entry', name)
    if prev is None:
        return False
    else:
        db.delete_one('Entry', name)
        return True

def num_equal_to(value):
    results = db.query_by_value('Entry', value)
    return len(results)

def clean():
    return db.clean()

# def append_cmd(stack_name, cmd):
#     entity = db.get('Length', stack_name)
#     index = entity['value']
#     print('index:', index)
#     if index is None:
#         index = 0
#     print('index:', index)
#     # increment index
#     index += 1
#     print('index:', index)
#     # db.set('Length', stack_name, index)
#     # db.set(stack_name, index, json.dumps(cmd))
#     # return index

# def pop_cmd(stack_name):
#     index = db.get('Length', stack_name)
#     cmd = db.get(stack_name, index)
#     # decrement index:
#     index -= 1
#     db.set('Length', stack_name, index)
#     return cmd

# clean()
# append_cmd('Undo', ('set', 'a', '1', None))
