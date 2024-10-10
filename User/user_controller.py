from app import app
from User.user_connector import User
from flask import request

user = User()

@app.route('/create-user', methods=['POST'])
def create_user():
    print('hello user?')
    return user.create_user_record(request.get_json())

@app.route('/get-users', methods=['GET'])
def get_users():
    return user.user_records()

@app.route('/get-user', methods=['POST'])
def get_user():
    return user.read_user_record_by_id(request.get_json())

@app.route('/update-user', methods=['PUT'])
def update_user():
    return user.update_user_record(request.get_json())

@app.route('/delete-user', methods=['PUT'])
def delete_user():
    return user.delete_user_record(request.get_json())