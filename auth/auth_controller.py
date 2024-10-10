from app import app
from flask import request
from auth.auth_connector import Auth
from utilities.helper_functions import Helper
from flask_jwt_extended import jwt_required, get_jwt_identity
from auth.auth_queries import auth_queries

auth = Auth()
util_object = Helper()

@app.route('/login-user', methods=['POST'])
def login():
    return auth.login_user(request.get_json())

@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    user = util_object.execute_query(auth_queries['IF_USER_EXISTS'], (current_user,))