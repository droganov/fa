from yoyo import read_migrations
from yoyo import get_backend

from app.config import config

backend = get_backend(config.database_url_yoyo)
migrations = read_migrations("sql/migrations")


async def run() -> None:
    """Applies migrations to the database."""
    print("Applying migrations... ")
    with backend.lock():
        backend.apply_migrations(backend.to_apply(migrations))

    print("Migrations applied.")
