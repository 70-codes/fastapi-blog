from passlib.context import CryptContext

# initializing the password cryptography
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    
    def bcrypt(password: str):
        return pwd_context.hash(password)
    
    def verify(hashed_password: str, plain_password: str):
        return pwd_context.verify(plain_password, hashed_password)
        