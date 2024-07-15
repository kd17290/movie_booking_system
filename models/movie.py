from models.base_model import BaseModel


class Movie(BaseModel):
    title: str
    description: str
    duration: int

    def __init__(
        self, title: str, description: str, duration: int, id: int | None = None
    ):
        super().__init__(id)
        self.title = title
        self.description = description
        self.duration = duration
