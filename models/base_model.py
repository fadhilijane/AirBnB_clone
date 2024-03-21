import uuid
import datetime

class BaseModel:
    def __init__(self):
        self.id = uuid.uuid4().hex
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = self.created_at
        self.soft_deleted = False

    def __str__(self):
        return self.to_dict()

    def save(self):
        self.updated_at = datetime.datetime.now().isoformat()

    def to_dict(self):
        a = self.__dict__
        return f'[{self.__class__}] ({self.id}) {a}'


