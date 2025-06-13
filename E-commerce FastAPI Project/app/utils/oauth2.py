from jose import JWTError, jwt
from datetime import datetime, timedelta
from app.User.schemas import TokenData
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.User.models import User


SECRET_KEY = "c3b66a8550de20d4304dd8e68bedf9611ef554d0a9b05feef1565573c937256b"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_EXPIRE_MIN = 60 * 24

def create_access_token(data: dict) -> str:
    """
    Create a JWT access token with an expiration time.

    Args:
        data (dict): Data to encode in the token.

    Returns:
        str: Encoded JWT token.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    jwt_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return jwt_token

def verify_access_token(token: str, credentials_exception: HTTPException) -> TokenData:
    """
    Verify the JWT access token and extract user information.

    Args:
        token (str): JWT token to verify.
        credentials_exception (HTTPException): Exception to raise if verification fails.

    Returns:
        TokenData: Token data containing user ID.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data = TokenData(id=id)
    except JWTError:
        raise credentials_exception
    return token_data

def get_current_user(token: str, credentials_exception: HTTPException) -> TokenData:
    """
    Get the current user from the JWT token.

    Args:
        token (str): JWT token.
        credentials_exception (HTTPException): Exception to raise if verification fails.

    Returns:
        TokenData: Token data containing user ID.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"www-Authenticate": "Bearer"}
    )
    return verify_access_token(token, credentials_exception)

def create_refresh_token(data: dict) -> str:
    """
    Create a JWT refresh token with a longer expiration time.

    Args:
        data (dict): Data to encode in the token.

    Returns:
        str: Encoded JWT refresh token.
    """
    to_encode = data.copy()
    to_encode.update({"exp": datetime.utcnow() + timedelta(minutes=REFRESH_EXPIRE_MIN)})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/signin")



def decode_token(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> User:
    """
    Decode the JWT token and return the corresponding user from the database.

    Args:
        token (str): JWT token.
        db (Session): Database session.

    Returns:
        User: The authenticated user object.

    Raises:
        HTTPException: If the token is invalid or user is not found.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get("user_id")
        if user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        user = db.query(User).filter(User.id == user_id).first()
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
        return user
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    
    