from datetime import datetime, timedelta, timezone
import jwt
from typing import Dict

from src.configs.jwt_configs import jwt_infos


class JwtHandler:
    def create_jwt_token(self, body: Dict = {}) -> str:
        return jwt.encode(
            payload={
                'exp': datetime.now(timezone.utc) + timedelta(hours=int(jwt_infos['JWT_HOURS'])),
                **body
            },
            key=jwt_infos['KEY'],
            algorithm=jwt_infos['ALGORITHM']
        )

    def decode_jwt_token(self, token: str) -> Dict:
        return jwt.decode(token, key=jwt_infos['KEY'], algorithms=[jwt_infos['ALGORITHM']])