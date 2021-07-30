from entry import *

# 2 stacks will be used here (LIFO):

# holds user commands => undo
done_commands = []

# holds undone commands => redo
undone_commands = []


def set(name, value):
    # Get previous val
    prevalue = get_entry('name')
    # Insert to stack
    done_commands.append(('set', name, value, prevalue))


def unset(name):
    # Get previous val
    prevalue = get_entry('name')
    # If prevalue is not None
    # Insert to stack
    done_commands.append(('unset', name, None, prevalue))


def undo():
    command = done_commands.pop()
    if command is not None:

        if command[0] == 'set':
            if command[3] is not None:
                # If a previous value existed
                set(command[1], command[3])
            else:
                unset(command[1])
        if command[0] == 'unset':
            set(command[1], command[2])

        # Insert to undone stack
        # Should value change?
        undone_commands.append(command)


def redo():
    command = undone_commands.pop()
    if command is not None:

        if command[0] == 'set':
            set(command[1], command[2])

        if command[0] == 'unset':
            unset(command[1], command[2])

        # Insert to done stack:
        # Should value change?
        done_commands.append(command)