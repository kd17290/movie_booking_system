import uuid

from models.base_model import BaseModel
from models.payment_status import PaymentStatus


class Payment(BaseModel):
    id: int | None
    txn: str | None
    booking_id: int
    amount: float
    currency: str
    payment_status: PaymentStatus

    def __init__(
        self,
        booking_id: int,
        amount: float,
        currency: str,
        payment_status: PaymentStatus = PaymentStatus.INITIATED,
        id: int | None = None,
    ):
        super().__init__(id)
        self.booking_id = booking_id
        self.amount = amount
        self.currency = currency
        self.payment_status = payment_status
        self.txn = uuid.uuid4().hex

    def set_payment_status(self, payment_status: PaymentStatus):
        self.payment_status = payment_status
