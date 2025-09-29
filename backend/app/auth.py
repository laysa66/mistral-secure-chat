from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
import hashlib
from app.models.schemas import UserInDB

#TODO: change this secret key to a strong random value and keep it safe in the .env file
SECRET_KEY = "SUPER_SECRET_KEY_CHANGE_ME"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# fake data base to test the authentication system
fake_users_db = {
    "admin": {
        "username": "admin",
        "email": "admin@example.com",
        "hashed_password": "2bb80d537b1da3e38bd30361aa855686bde0eacd7162fef6a25fe97bf527a25b",  # secret
        "disabled": False,
    },
    "testuser": {
        "username": "testuser",
        "email": "test@example.com", 
        "hashed_password": "2bb80d537b1da3e38bd30361aa855686bde0eacd7162fef6a25fe97bf527a25b",  # secret
        "disabled": False,
    }
}

def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        # simple hash verification using SHA256 to avoid any problemes with docker 
        password_hash = hashlib.sha256(plain_password.encode('utf-8')).hexdigest()
        return password_hash == hashed_password
    except Exception as e:
        print(f"Error verifying password: {e}")
        return False

def get_password_hash(password: str) -> str:
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def get_user(username: str) -> Optional[UserInDB]:
    if username in fake_users_db:
        user_dict = fake_users_db[username]
        return UserInDB(
            username=user_dict['username'],
            email=user_dict.get('email'),
            disabled=user_dict.get('disabled', False),
            hashed_password=user_dict['hashed_password']
        )
    return None

def authenticate_user(username: str, password: str) -> Optional[UserInDB]:
    
    print(f" Tentative de connexion pour: {username}")
    user = get_user(username)
    
    if not user:
        print(f" Utilisateur {username} non trouvé")
        return None
        
    password_valid = verify_password(password, user.hashed_password)
    print(f" Vérification mot de passe pour {username}: {'true password' if password_valid else 'false password'}") 
    
    if not password_valid:
        return None
        
    print(f"Authentification réussie pour {username}")
    return user

def create_user(username: str, password: str, email: Optional[str] = None) -> UserInDB:
   
    if username in fake_users_db:
        raise ValueError("User already exists")
    
    hashed_password = get_password_hash(password)
    user_dict = {
        "username": username,
        "email": email,
        "hashed_password": hashed_password,
        "disabled": False,
    }
    fake_users_db[username] = user_dict
    return UserInDB(
        username=username,
        email=email,
        disabled=False,
        hashed_password=hashed_password
    )

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            return None
        return payload
    except JWTError:
        return None
