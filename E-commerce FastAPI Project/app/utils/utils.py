from passlib.context import CryptContext
import uuid
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    Hash a plain password using bcrypt.

    Args:
        password (str): The plain password to hash.

    Returns:
        str: The hashed password.
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain password against a hashed password.

    Args:
        plain_password (str): The plain password to verify.
        hashed_password (str): The hashed password to compare against.

    Returns:
        bool: True if the password matches, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)

def generate_reset_token(expiry_minutes: int = 5) -> tuple[str, datetime]:
    """
    Generate a unique password reset token and its expiration time.

    Args:
        expiry_minutes (int, optional): Minutes until the token expires. Defaults to 15.

    Returns:
        tuple[str, datetime]: The reset token and its expiration datetime.
    """
    token = str(uuid.uuid4())
    expires_at = datetime.utcnow() + timedelta(minutes=expiry_minutes)
    return token, expires_at


