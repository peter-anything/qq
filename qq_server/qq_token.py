import jwt
from datetime import datetime, timedelta
import base64

class QQToken(object):
    private_key = open('id_rsa', 'rb').read()
    public_key = open('id_rsa.pub', 'rb').read()
    message = {
        'iss': 'https://qq.com/',
        'sub': 'all',
        'iat': 1485972805,
        'exp': 1485972805,
    }

    @classmethod
    def encode(cls, id):
        cls.message['id'] = id
        now = datetime.now()
        exp = now + timedelta(hours=2)
        cls.message['iat'] = int(now.timestamp())
        cls.message['exp'] = int(exp.timestamp())
        encoded_token = jwt.encode(cls.message, cls.private_key, algorithm='RS256')
        return str(encoded_token, encoding="utf-8")

    @classmethod
    def decode(cls, token):
        return jwt.decode(token, cls.public_key, algorithms='RS256')