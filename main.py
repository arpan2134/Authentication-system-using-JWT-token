from jwt_authenticator import jwt
from jwt_authenticator import MyAuthenticator
from jwt_authenticator import datetime

authenticator = MyAuthenticator('secret..key')
token = authenticator.authenticate('admin', 'password')

if token:
    print('Authentication successful. Token:', token)

    try:
        decoded_token = authenticator.verify_token(token)
        print('Token is valid.')

        if 'exp' in decoded_token:
            expiration_timestamp = decoded_token['exp']
            expiration_datetime = datetime.datetime.fromtimestamp(expiration_timestamp)
            print('Token expiration date:', expiration_datetime)

            current_time = datetime.datetime.utcnow()
            if current_time > expiration_datetime:
                print('Token has expired!')           

    except jwt.ExpiredSignatureError:
        print('Token has expired!')
    except jwt.InvalidTokenError:
        print('Invalid token.')
else:
    print('Authentication failed.')
