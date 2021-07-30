from pyasn1.type.constraint import ValueRangeConstraint
from database import Database
# import json


db = Database()


# 2 stacks will be used here (LIFO):

# holds user commands => undo
done_commands = []

# holds undone commands => redo
undone_commands = []


def get_entry(name):
    return db.get('Entry', name)


def set_entry(name, value):
    prevalue = None
    # Get previous val
    prev_entry = db.get('Entry', name)
    print('prev_entry: ', prev_entry)
    if prev_entry is not None and prev_entry['value'] is not None:
        prevalue = prev_entry['value']
    print('prevalue:', prevalue)
    res = db.set('Entry', name, value)
    print('set res: ', res)
    # Insert to stack
    tuple = ('set', name, value, prevalue)
    print('tuple: ', tuple)
    done_commands.append(tuple)
    print(f'done_commands: {done_commands}')


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


def undo():
    if len(done_commands) == 0:
        return False
    command = done_commands.pop()
    if command is not None:
        variable_name = command[1]
        new_value = None
        if command is not None:

            if command[0] == 'set':
                if command[3] is not None:
                    # If a previous value existed => set
                    db.set('Entry', command[1], command[3])
                    new_value = command[3]
                else:
                    # Else delete the entry:
                    db.delete_one('Entry', command[1])

            if command[0] == 'unset':
                db.set(command[1], command[3])
                new_value = command[3]

            # Insert to undone stack
            undone_commands.append(command)
            print(f'UNDO done_commands: {done_commands}')
            print(f'UNDO undone_commands: {undone_commands}')
            name_and_value = [variable_name, new_value]
            return name_and_value



