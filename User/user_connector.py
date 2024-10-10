import uuid
from hashlib import md5
from flask_jwt_extended import get_jwt_identity, jwt_required
from utilities.helper_functions import Helper
from utilities.custom_responses import CustomResponse
from utilities.validation import user_insertion_schema, user_updation_schema
from User.user_queries import user_queries
from cerberus import Validator

util_object = Helper()
response = CustomResponse()

class User:
    
    def create_user_record(self, data):
        try:
            v = Validator(user_insertion_schema)
            if not v.validate(data):
                return response.error_message(400, 'Validation error', v.errors)
            user_id = str(uuid.uuid4())
            encrypted_password = md5(str(data['password']).encode()).hexdigest()
            user_data = (user_id, data['name'], data['username'], encrypted_password, data['email'], data['phone_number'], data['dob'], data['role'])
            result = util_object.execute_query(user_queries['INSERT_USER'], user_data)
            if result:
                return response.success_message(200, 'User created successfully') 
            else:
                return response.error_message(400, 'User could not be created')
        except Exception as e:
            return str(e)
    
    @jwt_required()
    def read_user_record_by_id(self, data):
        try:
            username = data['username']
            current_user = get_jwt_identity()
            user = util_object.check_if_user_exists(current_user)
            response.if_not_authorised_user(user)
            if (user[0]['USERNAME']==username):
                result = util_object.execute_query(user_queries['GET_USER'],(username,))
                return response.success_message(200, 'User fetched successfully', result) 
            else:
                return response.error_message(400, 'User could not be fetched')
        except Exception as e:
            return str(e)

    @jwt_required()  
    def user_records(self):
        try:
            current_user = get_jwt_identity()
            user = util_object.check_if_user_exists(current_user)
            if (user[0]['ROLE']=='Admin'):
                result = util_object.execute_query(user_queries['GET_USERS'])
                return response.success_message(200, 'Users fetched successfully', result)
            else:
                return response.error_message(400, 'User does not have permission to view this')
        except Exception as e:
            return str(e)

    @jwt_required()
    def update_user_record(self, data):
        try:
            v = Validator(user_updation_schema)
            if not v.validate(data):
                return response.error_message(400, 'Validation error', v.errors)
            current_user = get_jwt_identity()
            user = util_object.check_if_user_exists(current_user)
            response.if_not_authorised_user(user)
            if (user[0]['USERNAME']==data['username']):
                new_user_data = (data['username'], data['password'], data['phone_number'], data['id'])
                result = util_object.execute_query(user_queries['UPDATE_USER'],new_user_data,)
                return response.success_message(200, 'User updated successfully', result) 
            else:
                return response.error_message(400, 'User could not be updated')
        except Exception as e:
            return str(e)

    @jwt_required()    
    def delete_user_record(self, data):
        try:
            username = data['username']
            current_user = get_jwt_identity()
            user = util_object.check_if_user_exists(current_user)
            response.if_not_authorised_user(user)
            if (user[0]['USERNAME']==username):
                result = util_object.execute_query(user_queries['DELETE_USER'],(username,))
                return response.success_message(200, 'User deleted successfully', result)
            else:
                return response.error_message(400, 'User could not be deleted')
        except Exception as e:
            return str(e)

  
