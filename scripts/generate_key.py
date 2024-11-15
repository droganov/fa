import base64
import secrets


def generate_key(length: int) -> str:
    """
    Generates a key of the specified length.
    """
    key = secrets.token_bytes(length)
    return base64.b64encode(key).decode("utf-8")


def print_generated_keys():
    """
    Prints the generated keys for the application.
    """

    print(f'A256GCM_KEY="{generate_key(32)}"')
    print(f'JWT_SECRET_KEY="{generate_key(64)}"')
    print(f'SESSION_SECRET_KEY="{generate_key(88)}"')
    print(f'SESSION_SALT="{generate_key(64)}"')


async def run() -> None:
    """
    Generates keys for the application.
    """

    print_generated_keys()
