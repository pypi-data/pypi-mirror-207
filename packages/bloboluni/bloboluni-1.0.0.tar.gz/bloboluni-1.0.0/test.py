from dataclasses import dataclass
from bloboluni.storage import JsonPickleBlobStorage
import os, uuid
from dotenv import load_dotenv
load_dotenv()

@dataclass
class MyProfession:
    name: str
    description: str

@dataclass
class MyClass:
    name: str
    age: int
    profession: MyProfession

if __name__ == "__main__":
    data = MyClass("blob", 30, MyProfession("Developer", "A developer"))

    connectionstring = os.environ["AZURE_STORAGE_CONNECTION_STRING"]
    storage = JsonPickleBlobStorage(connectionstring, "langchain")
    
    key = uuid.uuid4().hex
    blob = storage.get(key)
    assert blob is None
    storage.upsert(key, data)
    blob = storage.get(key)
    assert blob is not None
    storage.delete(key)
    blob = storage.get(key)
    assert blob is None