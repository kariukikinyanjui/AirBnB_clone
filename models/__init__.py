#!/usr/bin/python3
"""Create a unique 'FileStorage' instance for the application."""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()


from models.base_model import BaseModel
models = {
    'BaseModel': BaseModel,
    }
