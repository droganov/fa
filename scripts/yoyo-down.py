from yoyo import read_migrations
from yoyo import get_backend

from app.config import config

backend = get_backend(config.database_url_yoyo)
migrations = read_migrations("src/migrations")


async def run() -> None:
    """Applies migrations to the database."""
    print("Rolling back migrations...")
    with backend.lock():
        backend.rollback_migrations(backend.to_rollback(migrations))

    print("Migrations rolled back.")
