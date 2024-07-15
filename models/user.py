from models.base_model import BaseModel


class User(BaseModel):
    username: str
    email: str
    password: str
    is_active: bool

    def __init__(self, username: str, email: str, password: str, id: int | None = None):
        super().__init__(id)
        self.username = username
        self.email = email
        self.password = password
        self.is_active = True
