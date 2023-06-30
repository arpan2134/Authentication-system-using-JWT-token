from jwt_authenticator import MyAuthenticator

authenticator = MyAuthenticator('secret..key')
token = authenticator.authenticate('admin', 'password')
if token:
    print('Authentication successful. Token:', token)
else:
    print('Authentication failed.')
