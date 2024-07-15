from models.show import Show
from repositories.in_memory_repository import InMemoryRepository


class ShowRepository(InMemoryRepository[Show]):
    pass
