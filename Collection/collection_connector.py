from flask_jwt_extended import get_jwt_identity, jwt_required
from utilities.helper_functions import Helper
from utilities.custom_responses import CustomResponse
from utilities.validation import collection_insertion_schema
from utilities.log import setup_logger
from auth.auth_queries import auth_queries
from Collection.collection_queries import collection_queries, book_collection_queries
from cerberus import Validator

util_object = Helper()
response = CustomResponse()
error_logger  = setup_logger('error.log')

class Collection:
    
    @jwt_required()
    def create_collection_record(self, data):
        try:
            v = Validator(collection_insertion_schema)
            if not v.validate(data):
                return response.error_message(400, 'Validation error', v.errors)
            current_user = get_jwt_identity()
            user = util_object.execute_query(auth_queries['IF_USER_EXISTS'], (current_user,))
            if (user[0]['ROLE']=='Customer'):
                result = util_object.execute_query(collection_queries['INSERT_USER_COLLECTION'], data)
                return response.success_message(200, 'User collection created successfully', result) if result else response.error_message(400, 'User collection could not be created')
            else:
                result = util_object.execute_query(collection_queries['INSERT_GLOBAL_COLLECTION'], data)
                return response.success_message(200, 'Global collection created successfully', result) if result else response.error_message(400, 'Global collection could not be created')
        except Exception as e:
            return str(e)
        
    @jwt_required()   
    def create_book_collection(self, data):
        try:
            current_user = get_jwt_identity()
            user = util_object.execute_query(auth_queries['IF_USER_EXISTS'], (current_user,))
            if (user[0]['ROLE']=='Customer'):
                result = util_object.execute_query(book_collection_queries['INSERT_COLLECTION'],data)
                return response.success_message(200, 'Book-collection created successfully', result)
            else:
                return response.error_message(400, 'Book-collection could not be created')
        except Exception as e:
            return str(e)
        
    @jwt_required()
    def read_collection_records(self):
        try:
            current_user = get_jwt_identity()
            user = util_object.execute_query(auth_queries['IF_USER_EXISTS'], (current_user,))
            if user:
                result = util_object.execute_query(collection_queries['GET_GLOBAL_COLLECTIONS'])
                return response.success_message(200, 'Collection fetched successfully', result) 
            else: 
                error_logger.error('%s raised an error')
                return response.error_message(400, 'Collection could not be fetched')
        except Exception as e:
            return str(e)
        
    @jwt_required()
    def get_collection_by_user(self, data):
        try:
            current_user = get_jwt_identity()
            user = util_object.execute_query(auth_queries['IF_USER_EXISTS'], (current_user,))
            collection_owner = util_object.execute_query(collection_queries['FIND_COLLECTION'], (user[0]['ID']))
            if collection_owner:
                user_id = list(data.values())
                result = util_object.execute_query(book_collection_queries['GET_COLLECTION_BY_USER'], user_id)
                return response.success_message(200, 'Collection fetched successfully', result)
            else:
                return response.error_message(400, 'Collection could not be fetched') 
        except Exception as e:
            return str(e)

    @jwt_required()
    def update_collection_record(self, data):
        try:
            current_user = get_jwt_identity()
            user = util_object.execute_query(auth_queries['IF_USER_EXISTS'], (current_user,))
            collection_owner = util_object.execute_query(collection_queries['FIND_COLLECTION'], (user[0]['ID']))
            if collection_owner:
                result = util_object.execute_query(collection_queries['UPDATE_COLLECTION'],data)
                return response.success_message(200, 'Collection updated successfully', result)
            else:
                return response.error_message(400, 'Collection could not be updated')
        except Exception as e:
            return str(e)
    
    @jwt_required()
    def get_books_from_collection(self, data):
        try:
            current_user = get_jwt_identity()
            user = util_object.execute_query(auth_queries['IF_USER_EXISTS'], (current_user,))
            collection_owner = util_object.execute_query(collection_queries['FIND_COLLECTION'], (user[0]['ID']))
            if collection_owner:
                collection_id = list(data.values())
                result = util_object.execute_query(book_collection_queries['GET_BOOKS_FROM_COLLECTION'], collection_id)
                return response.success_message(200, 'Books of collection fetched successfully', result)
            else:
                return response.error_message(400, 'Books of collection could not be fetched')
        except Exception as e:
            return str(e)  
    
    @jwt_required()
    def delete_book_from_collection(self, data):
        try:
            current_user = get_jwt_identity()
            user = util_object.execute_query(auth_queries['IF_USER_EXISTS'], (current_user,))
            collection_owner = util_object.execute_query(collection_queries['FIND_COLLECTION'], (user[0]['ID']))
            if collection_owner:
                result = util_object.execute_query(book_collection_queries['DELETE_BOOK_FROM_COLLECTION'],data)
                return response.success_message(200, 'Collection deleted successfully', result)
            else:
                return response.error_message(400, 'Collection could not be deleted')
        except Exception as e:
            return str(e)
