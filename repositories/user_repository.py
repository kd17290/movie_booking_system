from models.user import User
from repositories.in_memory_repository import InMemoryRepository


class UserRepository(InMemoryRepository[User]):
    pass
