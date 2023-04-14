import jwt
import datetime

from config import JWT_SECRET, JWT_EXPIRED_SECOND, JWT_REFRESH_SECOND

def create_token(id, role):
    return jwt.encode({
        "id": id,
        "role": role,
        "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(seconds=JWT_EXPIRED_SECOND),
    }, JWT_SECRET, algorithm="HS256")

def token_validate(token):
    return jwt.decode(token, JWT_SECRET, algorithms=["HS256"])

def check_expired(exp):
    expired = exp - int((datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(seconds=JWT_REFRESH_SECOND)).timestamp())
    if expired < 0:
        return True
    return False
