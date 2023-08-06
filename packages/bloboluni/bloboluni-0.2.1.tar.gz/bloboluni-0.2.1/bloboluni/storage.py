import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import abc
from typing import Generic, TypeVar
from serializers import ISerializer, JsonSerializer, JsonPickleSerializer

T = TypeVar('T')
    
class BlobStorage(Generic[T]):
    def __init__(self, connectionstring: str, container: str, serializer: ISerializer = None):
        self.connectionstring = connectionstring
        self.container = container
        self.serializer = serializer
        
    def get(self, key: str) -> None | T:
        blob = BlobClient.from_connection_string(conn_str=self.connectionstring, container_name=self.container, blob_name=key)
        if blob.exists():
            content = blob.download_blob().readall()
            if self.serializer is None:
                return content
            return self.serializer.deserialize(content)
            
        return None
    
    def upsert(self, key: str, data: T) -> BlobClient:
        container = ContainerClient.from_connection_string(conn_str=self.connectionstring, container_name=self.container)
        if container is None or not container.exists():
            container.create_container()
        
        serialized = data
        if self.serializer is not None:
            serialized = self.serializer.serialize(data)
        
        blob = container.get_blob_client(key)
        blob.upload_blob(serialized, overwrite=True)
        return blob
    
    def delete(self, key: str) -> None:
        blob = BlobClient.from_connection_string(conn_str=self.connectionstring, container_name=self.container, blob_name=key)
        blob.delete_blob()
    
class JsonBlobStorage(BlobStorage):
    def __init__(self, connectionstring: str, container: str):
        super().__init__(connectionstring, container, JsonSerializer())
        
class JsonPickleBlobStorage(BlobStorage):
    def __init__(self, connectionstring: str, container: str):
        super().__init__(connectionstring, container, JsonPickleSerializer())