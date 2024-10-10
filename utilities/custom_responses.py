from flask import jsonify

class CustomResponse:

    def success_message(self, status_code, message, data=None):
       return jsonify({'status': status_code, 'message': message, 'data': data})
    
    def error_message(self, status_code, message, data=None):
        return jsonify({'status': status_code, 'message': message, 'data': data})
    
    def if_not_authorised_user(self, user):
        if not user:
            return jsonify({'status': '400', 'message': 'User does not have permission to view this'})

    
    