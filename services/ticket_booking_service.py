from exceptions import ShowNotFound, SeatAlreadyBooked, UserNotFound, SeatNotFound
from models.booking import Booking
from models.booking_status import BookingStatus
from models.payment import Payment
from models.payment_status import PaymentStatus
from models.seat import Seat
from models.seat_status import SeatStatus
from models.show import Show
from models.user import User
from payment_gateway.gateway import PaymentGateway
from repositories.booking_repository import BookingRepository
from repositories.show_repository import ShowRepository
from repositories.user_repository import UserRepository


class TicketBookingService:
    show_repository: ShowRepository
    user_repository: UserRepository
    booking_repository: BookingRepository
    payment_gateway: PaymentGateway

    def __init__(self, payment_gateway: PaymentGateway):
        print(f"Initializing TicketBookingService...")
        self.payment_gateway = payment_gateway
        self.show_repository = ShowRepository()
        self.user_repository = UserRepository()
        self.booking_repository = BookingRepository()

    def book_ticket(
        self, user_id: int, show_id: int, selected_seat_ids: list[int]
    ) -> Booking:
        print(f"Booking {show_id} for {user_id}")
        user: User | None = self.user_repository.find_by_pk(user_id)
        if not user:
            raise UserNotFound("Show not found")
        show: Show | None = self.show_repository.find_by_pk(show_id)
        if not show:
            raise ShowNotFound("Show not found")
        selected_seats: list[Seat] = []
        for selected_seat_id in selected_seat_ids:
            seat = show.seats.get(selected_seat_id, None)
            if not seat:
                raise SeatNotFound("Seat not found")
            if seat.seat_status != SeatStatus.AVAILABLE:
                raise SeatAlreadyBooked("Seat already booked")
            selected_seats.append(seat)
        print(f"Validations completed...")
        total_price = sum([seat.price for seat in selected_seats])
        booking = Booking(
            user=user,
            show=show,
            seats=selected_seats,
            total_price=total_price,
        )
        booking = self.booking_repository.save(booking)
        print(f"Attempting payment for {booking.show.id}")
        payment: Payment = self.payment_gateway.make_payment(
            booking_id=booking.id, amount=booking.total_price, currency="INR"
        )
        booking.set_payment(payment)
        self.booking_repository.update(booking)
        if payment.payment_status == PaymentStatus.SUCCESS:
            print(f"Payment successful")
            for seat in selected_seats:
                seat.seat_status = SeatStatus.BOOKED
                show.seats[seat.id] = seat
            self.show_repository.update(show)
            booking.set_booking_status(BookingStatus.CONFIRMED)
            self.booking_repository.update(booking)
        else:
            print("Payment failed")
            booking.set_booking_status(BookingStatus.CANCELLED)
            self.booking_repository.update(booking)
        return booking
