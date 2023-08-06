from dataclasses import dataclass
from storage import JsonPickleBlobStorage
import os
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
    data = MyClass("John", 30, MyProfession("Developer", "A developer"))

    connectionstring = os.environ["AZURE_STORAGE_CONNECTION_STRING"]
    storage = JsonPickleBlobStorage(connectionstring, "langchain")
    
    storage.upsert("john", data)
    john = storage.get("john")
    storage.delete("john")