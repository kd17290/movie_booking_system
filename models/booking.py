from models.base_model import BaseModel
from models.booking_status import BookingStatus
from models.payment import Payment
from models.seat import Seat
from models.show import Show
from models.user import User


class Booking(BaseModel):
    user: User
    show: Show
    seats: list[Seat]
    total_price: float
    booking_status: BookingStatus
    payment: Payment | None = None

    def __init__(
        self,
        user: User,
        show: Show,
        seats: list[Seat],
        total_price: float,
        booking_status: BookingStatus,
        id: int | None = None,
    ):
        super().__init__(id)
        self.user = user
        self.show = show
        self.seats = seats
        self.total_price = total_price
        self.booking_status = booking_status
        self.payment = None

    def set_booking_status(self, booking_status: BookingStatus):
        self.booking_status = booking_status

    def set_payment(self, payment: Payment):
        self.payment = payment

    def __str__(self):
        return f"{self.id}: {self.total_price} {self.booking_status}"
