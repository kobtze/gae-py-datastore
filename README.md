# PY DATASTORE
Very basic implementation of Datastore service.
The service consists of the following building blocks:

## Main / EntryController
Handles HTTP requests, validates input, formats output, Relies on **Entry App**
- [X] /get
- [X] /set
- [X] /unset
- [X] /numequalto
- [X] /undo
- [ ] /redo
- [X] /end
- [X] _response

## Entry App
Relies on **DBService**, handles Entry operations, makes higher-level computations
- [X] get_entry
- [X] set_entry
- [X] unset_entry
- [X] num_equal_to
- [X] clean
- [X] undo
- [ ] redo

## Database Service
Low-level handling of DB operations
- [X] get(id)
- [X] query(param)
- [X] set(id)
- [X] delete(id)
- [X] delete
