from models.payment import Payment
from repositories.in_memory_repository import InMemoryRepository


class PaymentRepository(InMemoryRepository[Payment]):
    pass
