"""Configuration settings for the application."""

from pydantic_settings import BaseSettings
import time
from hashlib import sha256
from os import getenv


class Config(BaseSettings):
    """Configuration settings for the application."""

    a256Gcm_key: str
    bugsnag_api_key: str | None = None
    database_url: str
    jwt_secret_key: str
    session_cookie_key: str = "xid"
    session_max_age_in_seconds: int = 129600
    session_secret_key: str
    session_salt: str

    @property
    def jwt_random_key(self):
        """Generates a random key for JWT token."""
        current_timestamp = time.time()
        interval_in_seconds = 30 * 60
        key_interval = int(current_timestamp) // interval_in_seconds
        random_key = self.jwt_secret_key + str(key_interval)
        new_key = sha256(random_key.encode()).hexdigest()
        return new_key

    @property
    def database_url_yoyo(self):
        """Returns the database URL for yoyo."""
        return self.database_url.replace("postgresql://", "postgresql+psycopg://")

    class Config:
        """Pydantic configuration settings."""

        env_file = getenv("ENV_FILE", ".env")
        env_prefix = ""
        extra = "allow"


config = Config()
