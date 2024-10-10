from app import app
from flask import request
from Collection.collection_connector import Collection

collection = Collection()

@app.route('/create-collection', methods=['POST'])
def create_collection():
    return collection.create_collection_record(request.get_json())

@app.route('/get-collections', methods=['GET'])
def get_collection():
    return collection.read_collection_records()

@app.route('/update-collection', methods=['PUT'])
def update_collection():
    return collection.update_collection_record(request.get_json())

@app.route('/create-book-collection', methods=['POST'])
def create_book_collection_entry():
    return collection.create_book_collection(request.get_json())

@app.route('/delete-collection', methods=['PUT'])
def delete_book_in_collection():
    return collection.delete_book_from_collection(request.get_json())

@app.route('/get-user-collection', methods=['POST'])
def get_user_collection():
    return collection.get_collection_by_user(request.get_json())

@app.route('/get-books-from-collection', methods=['POST'])
def get_books_collection():
    return collection.get_books_from_collection(request.get_json())