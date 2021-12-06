# JsonDB
dictionary object that is easily stored and loaded from json file type

## Class methods:
### __init__()
when costracting the object you are required to pass a path to an existing or a location where the new json file will be stored

### store()
After updating the dictionary you can store changes to memory using this method.
If another instance of the object changed the file in the mean time the changes will be loaded to the object before storing the changes

### load()
loads the current state of the object. This is automatically done while storing.
