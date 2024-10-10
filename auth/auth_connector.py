from hashlib import md5
from app import app
from utilities.helper_functions import Helper
from utilities.custom_responses import CustomResponse
from auth.auth_queries import auth_queries
from flask_jwt_extended import create_access_token
from datetime import timedelta

util_object = Helper()
response = CustomResponse()

class Auth:
    def login_user(self, data):
        username = data['username']
        password = data['password']
        result = util_object.execute_query(auth_queries['IF_USER_EXISTS'],(username,))
        user_name = result[0]['USERNAME']
        role = result[0]['ROLE']
        print(result)
        expires_in = timedelta(days=1)
        if (result[0]['PASSWORD']== (md5(str(password).encode())).hexdigest()):
            access_token = create_access_token(identity=user_name, additional_claims={'role': role}, expires_delta=expires_in)
            return response.success_message(200, 'Token', access_token) if access_token else response.error_message(400, 'Token could not be fetched')
        else:
            return response.error_message(400, 'User details are incorrect')