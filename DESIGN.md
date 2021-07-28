# PY DATASTORE
Very basic implementation of Datastore service.
The service consists of the following building blocks:

## Main / EntryController
Relies on **EntryService** & **HistoryService**, handles HTTP requests, validates input, formats output
> Holds **Request** Class
- [ ] /get
- [ ] /set
- [ ] /unset
- [ ] /numequalto
- [ ] /undo
- [ ] /redo
- [ ] /end

## Entry Service
Relies on **DBService**, handles Entry operations, makes higher-level computations
- [ ] get_entry
- [ ] set_entry
- [ ] unset_entry
- [ ] num_equal_to
- [ ] clean

## History Service
Stores undo_stack, redo_stack
> Holds **Stack** & **Node** Classes
- [ ] undo
- [ ] redo

## Database Service
Low-level handling of DB operations
- [ ] get(id)
- [ ] query(param)
- [ ] set(id)
- [ ] delete(id) 
