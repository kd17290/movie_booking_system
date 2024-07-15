from enum import Enum


class PaymentStatus(Enum):
    INITIATED = "INITIATED"
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"
