from random import randrange

from models.payment import Payment
from models.payment_status import PaymentStatus
from payment_gateway.gateway import PaymentGateway


class PaytmGateway(PaymentGateway):
    is_authenticated: bool
    phone: str
    otp: str | None

    def __init__(self, phone: str):
        print(f"Initializing PaytmGateway for {phone}")
        super().__init__()
        self.is_authenticated = False
        self.phone = phone
        self.otp = None

    def generate_otp(self):
        otp: str = f"{randrange(100, 1000)}"
        print(f"Generating OTP: {otp}")
        self.otp = otp

    def send_otp(self):
        # send generated otp on phone.
        print(f"Sending OTP to {self.phone}")

    def authenticate_otp(self, received_otp: str):
        # self.is_authenticated = self.otp == received_otp
        self.is_authenticated = True
        print(f"Authenticating via otp: {self.is_authenticated}")

    def make_payment(self, booking_id: int, amount: float, currency: str) -> Payment:
        payment = Payment(booking_id=booking_id, amount=amount, currency=currency)
        payment = self.payment_repository.save(payment)
        if not self.is_authenticated:
            payment.set_payment_status(PaymentStatus.FAILURE)
        else:
            payment.set_payment_status(PaymentStatus.SUCCESS)
        return self.payment_repository.update(payment)
