from flask_jwt_extended import get_jwt_identity, jwt_required
from utilities.helper_functions import Helper
from utilities.custom_responses import CustomResponse
from utilities.validation import book_schema
from cerberus import Validator
from Book.book_queries import book_queries

util_object = Helper()
response = CustomResponse()

class Book:
    
    @jwt_required()
    def create_book_record(self, data):
        try:
            v = Validator(book_schema)
            if not v.validate(data):
                return response.error_message(400, 'Validation error', v.errors)
            current_user = get_jwt_identity()
            user = util_object.check_if_user_exists(current_user)
            if (user):
                result = util_object.execute_query(book_queries['INSERT_BOOK'],data)
                return response.success_message(200, 'Book created successfully', result)
            else:
                return response.error_message(400, 'Book could not be created')
        except Exception as e:
            return str(e)
        

    @jwt_required()
    def read_book_record_by_id(self, data):
        try:
            record_id = data['id']
            current_user = get_jwt_identity()
            user = util_object.check_if_user_exists(current_user)
            if(user):
                result = util_object.execute_query(book_queries['GET_BOOK'],(record_id,))
                return response.success_message(200, 'Book fetched successfully', result)
            else:
                return response.error_message(400, 'Book could not be fetched')
        except Exception as e:
            return str(e)

    @jwt_required()
    def update_book_record(self, data):
        try:
            v = Validator(book_schema)
            if not v.validate(data):
                return response.error_message(400, 'Validation error', v.errors)
            current_user = get_jwt_identity()
            user = util_object.check_if_user_exists(current_user)
            book_owner = util_object.execute_query(book_queries['FIND_BOOK'], (user[0]['ID'],))
            if book_owner:
                result = util_object.execute_query(book_queries['UPDATE_BOOK'],data)
                return response.success_message(200, 'User updated successfully', result)
            else:
                response.if_not_authorised_user(user)
                return response.error_message(400, 'Book could not be updated')
        except Exception as e:
            return str(e)

    @jwt_required()
    def delete_book_record(self, record_id):
        try:
            current_user = get_jwt_identity()
            user = util_object.check_if_user_exists(current_user)
            book_owner = util_object.execute_query(book_queries['FIND_BOOK'], (user[0]['ID'],))
            if book_owner:
                result = util_object.execute_query(book_queries['DELETE_BOOK'],record_id)
                return response.success_message(200, 'Book deleted successfully', result) 
            else:
                return response.error_message(400, 'Book could not be deleted')
        except Exception as e:
            return str(e)
    
    @jwt_required()
    def search_book_record(self, data):
        try:
            current_user = get_jwt_identity()
            user = util_object.check_if_user_exists(current_user)
            if user:
                conditions = []
                search_data = []

                if 'genre' in data:
                    conditions.append("GENRE=%s")
                    search_data.append(data['genre'])
                if 'author' in data:
                    conditions.append("AUTHOR=%s")
                    search_data.append(data['author'])
                
                where_clause = " OR ". join(conditions)
                query = f"SELECT TITLE, AUTHOR, ADDED_AT, PRICE FROM BOOKS WHERE {where_clause} ORDER BY ADDED_AT DESC, PRICE ASC"
                result = util_object.execute_query(query, tuple(search_data))
                return response.success_message(200, 'Books found successfully', result)
            else: 
                return response.error_message(400, 'Books could not be found')
        except Exception as e:
            return str(e)
