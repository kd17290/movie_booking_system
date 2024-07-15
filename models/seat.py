from models.base_model import BaseModel
from models.seat_status import SeatStatus
from models.seat_type import SeatType


class Seat(BaseModel):
    row: str
    col: str
    seat_type: SeatType
    price: float
    seat_status: SeatStatus

    def __init__(
        self,
        row: str,
        col: str,
        seat_type: SeatType,
        price: float,
        seat_status: SeatStatus,
        id: int | None = None,
    ):
        super().__init__(id)
        self.row = row
        self.col = col
        self.seat_type = seat_type
        self.price = price
        self.seat_status = seat_status
