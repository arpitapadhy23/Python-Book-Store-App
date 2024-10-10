from app import app
from flask import request
from Book.book_connector import Book

book = Book()

@app.route('/create-book', methods=['POST'])
def create_book():
    return book.create_book_record(request.get_json())

@app.route('/get-book', methods=['POST'])
def get_book():
    return book.read_book_record_by_id(request.get_json())

@app.route('/update-book', methods=['PUT'])
def update_book():
    return book.update_book_record(request.get_json())

@app.route('/delete-book', methods=['PUT'])
def delete_book():
    return book.delete_book_record(request.get_json())

@app.route('/search-book', methods=['POST'])
def search_book():
    author = request.args.get('author')
    genre = request.args.get('genre')
    return book.search_book_record({'author': author, 'genre': genre})