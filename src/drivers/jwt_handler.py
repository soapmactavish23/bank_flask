from datetime import datetime, timedelta, timezone
import jwt
from typing import Dict


class JwtHandler:
    def create_jwt_token(self, body: Dict = {}) -> str:
        return jwt.encode(
            payload={
                'exp': datetime.now(timezone.utc) + timedelta(minutes=1),
                **body
            },
            key='minhaChave',
            algorithm='HS256'
        )

    def decode_jwt_token(self, token: str) -> Dict:
        return jwt.decode(token, key='minhaChave', algorithms=['HS256'])