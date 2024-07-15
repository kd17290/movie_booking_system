from models.base_model import BaseModel


class BookingStatus(BaseModel):
    CONFIRMED = "CONFIRMED"
    PENDING = "PENDING"
    CANCELLED = "CANCELLED"
