from flask import Flask
import os
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
jwt = JWTManager(app)

from User import user_controller
from Book import book_controller
from Collection import collection_controller
from auth import auth_controller

if __name__ == "__main__":
    app.run(debug=True)