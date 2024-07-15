from datetime import datetime

from models.base_model import BaseModel
from models.movie import Movie
from models.seat import Seat
from models.theater import Theater


class Show(BaseModel):
    theater: Theater
    movie: Movie
    start_time: datetime
    end_time: datetime
    seats: dict[int, Seat]

    def __init__(
        self,
        theater: Theater,
        movie: Movie,
        start_time: datetime,
        end_time: datetime,
        seats: list[Seat],
        id: int | None = None,
    ):
        super().__init__(id)
        self.theater = theater
        self.movie = movie
        self.start_time = start_time
        self.end_time = end_time
        self.seats = {}
        for seat in seats:
            self.seats[seat.id] = seat
