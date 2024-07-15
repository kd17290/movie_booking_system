from abc import ABC, abstractmethod

from models.payment import Payment
from repositories.payment_repository import PaymentRepository


class PaymentGateway(ABC):
    payment_repository: PaymentRepository

    def __init__(self):
        self.payment_repository = PaymentRepository()

    @abstractmethod
    def make_payment(self, booking_id: int, amount: float, currency: str) -> Payment:
        pass
