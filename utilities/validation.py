user_insertion_schema={
    'name': {'type': 'string', 'required': True},
    'username': {'type': 'string', 'required': True},
    'password': {'type': 'string', 'required': True, 'minlength': 8,'regex': r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'},
    'email': {'type': 'string', 'required': True, 'regex': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'},
    'phone_number': {'type': 'string', 'required': True},
    'dob': {'type': 'string', 'required': True, 'regex': r'^\d{4}-\d{2}-\d{2}$'},
    'role': {'type': 'string', 'required': True}
}

user_updation_schema={
    'username': {'type': 'string', 'required': True},
    'password': {'type': 'string', 'required': True, 'minlength': 8,'regex': r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'},
    'phone_number': {'type': 'string', 'required': True},
}

book_schema={
    'title': {'type': 'string', 'required': True},
    'author': {'type': 'string', 'required': True},
    'price': {'type': 'float', 'required': True},
    'isbn_no': {'type': 'string'},
    'summary': {'type': 'string'},
    'genre': {'type': 'string'},
    'id': {'type': 'number'}
}

collection_insertion_schema={
    'name': {'type':'string', 'required': True}
}


