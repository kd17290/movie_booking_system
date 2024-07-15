from models.booking import Booking
from repositories.in_memory_repository import InMemoryRepository


class BookingRepository(InMemoryRepository[Booking]):
    pass
