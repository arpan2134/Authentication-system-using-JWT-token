import jwt
import datetime

class JWTAuthenticator:
    def __init__(self, secret_key):
        self.secret_key = secret_key

    def gennerate_token(self, payload):
        token = jwt.encode(payload, self.secret_key, algorithm='HS256')
        return token
    
    def verify_token(self, token):
        try:
            decoded_token = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return decoded_token
        except jwt.ExpiredSignatureError:
            print('Token has been expired!!')
        except jwt.InvalidTokenError:
            print('Invalid token')



class MyAuthenticator(JWTAuthenticator):
        def __init__(self, secret_key):
            super().__init__(secret_key)

        def authenticate(self, username, password):
            if username == 'admin' and password == 'password':
                ###gen JWT token witthh user information 

                payload = {
                    'user_id': 1,
                    'username': username,
                    'exp' : datetime.datetime.utcnow() + datetime.timedelta(days=1)
                }
                token = self.gennerate_token(payload)
                return token
            else:
                return None
