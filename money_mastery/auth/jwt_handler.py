from typing import Dict, Any
from jose import jwt
from datetime import datetime, timedelta
from pytz import timezone

class JWTHandler:
    def __init__(self, secret_key: str):
        self.secret_key = secret_key

    def create_token(self, email: str) -> str:
        timezone_sp = timezone('America/Sao_Paulo')
        expira = datetime.now(tz=timezone_sp) + timedelta(
        minutes=60*24*7
    )
        jwt_config = {
            "exp": expira,
            "iat": datetime.now(tz=timezone_sp),
            "sub": str(email)
        }
        jwt_token = jwt.encode(jwt_config, self.secret_key, algorithm='HS256')

        return jwt_token

    def decode_token(self, token: str) -> Dict[str, Any]:
        decoded_token = jwt.decode(token, self.secret_key, algorithms=['HS256'])

        return decoded_token

