from datetime import datetime

from models import payment
from models.booking import Booking
from models.movie import Movie
from models.seat import Seat
from models.seat_status import SeatStatus
from models.seat_type import SeatType
from models.show import Show
from models.theater import Theater
from models.user import User
from payment_gateway.paytm import PaytmGateway
from repositories.seat_repository import SeatRepository
from repositories.show_repository import ShowRepository
from repositories.user_repository import UserRepository
from services.ticket_booking_service import TicketBookingService


def booking_demo():
    show_repository = ShowRepository()
    user_repository = UserRepository()
    seat_repository = SeatRepository()
    user: User = User(username="username", password="password", email="<EMAIL>")
    user = user_repository.save(user)

    seat_1: Seat = Seat(
        row="A",
        col="1",
        seat_type=SeatType.NORMAL,
        price=130,
        seat_status=SeatStatus.AVAILABLE,
    )
    seat_repository.save(seat_1)

    seat_2: Seat = Seat(
        row="A",
        col="1",
        seat_type=SeatType.PREMIUM,
        price=180,
        seat_status=SeatStatus.AVAILABLE,
    )
    seat_repository.save(seat_2)

    movie: Movie = Movie(
        title="first movie title", description="first movie description", duration=180
    )
    theater: Theater = Theater(name="first theater", address="first theater address")
    show: Show = Show(
        theater=theater,
        movie=movie,
        start_time=datetime.now(),
        end_time=datetime.now(),
        seats=[seat_1, seat_2],
    )
    show = show_repository.save(show)
    payment_gateway: payment = PaytmGateway(phone="1234567890")

    # First booking request
    payment_gateway.generate_otp()
    payment_gateway.send_otp()
    payment_gateway.authenticate_otp(received_otp="123456")
    ticket_booking_service = TicketBookingService(payment_gateway=payment_gateway)
    booking: Booking = ticket_booking_service.book_ticket(
        user_id=user.id, show_id=show.id, selected_seat_ids=[seat_2.id]
    )
    print(booking.__dict__)
    print(booking.payment.__dict__)

    # Another booking request
    payment_gateway.generate_otp()
    payment_gateway.send_otp()
    payment_gateway.authenticate_otp(received_otp="123456")
    booking: Booking = ticket_booking_service.book_ticket(
        user_id=user.id, show_id=show.id, selected_seat_ids=[seat_1.id]
    )
    print(booking.__dict__)


if __name__ == "__main__":
    booking_demo()
