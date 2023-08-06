# bloboluni: Azure blob storage wrapper
`bloboluni` is a simple python module for interacting with Azure blob storage.

## Installation
````
pip install bloboluni
````

## Usage
````python
from bloboluni.storage import JsonPickleBlobStorage
from mymodels import Person, Profession

if __name__ == "__main__":
    alex = Person("Alex", 27, Profession("Developer", "A developer"))

    # Create a storage client
    storage = JsonPickleBlobStorage(connectionstring="...", container="mycontainer")

    # Store some data
    storage.upsert(key="Alex", alex)

    # Read some data
    sam = storage.get(key="Sam") # Returns instance of Person or None

    # Delete some data
    storage.delete(key="Sam")
````

`bloboluni` provides storage clients using several different serialization implementations. 
Currently, these are:
- `BlobStorage`
- `JsonBlobStorage` 
- `JsonPickleBlobStorage`