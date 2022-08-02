#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods for other classes"""


import uuid
from datetime import datetime


class BaseModel:
    """BaseModel that defines all common attributes/methods for other classes"""
    def __init__.py:
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
