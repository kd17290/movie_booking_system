from models.booking import Booking
from models.seat import Seat
from repositories.in_memory_repository import InMemoryRepository


class SeatRepository(InMemoryRepository[Seat]):
    pass
