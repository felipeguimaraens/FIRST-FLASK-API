from flask import Flask, request, make_response
from flask_restful import Api, Resource, abort, reqparse
from functools import wraps

app = Flask(__name__)
api = Api(app)

BOOKS = {
    'book_1': {'title': 'Dom Casmurro', 'year': '1899'},
    'book_2': {'title': 'The Posthumous Memoris of Bras Cubas', 'year': '1881'},
    'book_3': {'title': 'The Fortune-Teller', 'year': '1884'},
    'book_4': {'title': 'Quincas Borba', 'year': '1891'},
    'book_5': {'title': 'O alienista', 'year': '1882'}
}

def login_required(event):
    @wraps(event)
    def login(*kargs, **kwargs):
        if request.authorization and \
        request.authorization.username == 'machado' and \
            request.authorization.password == 'deassis123':
            return event(*kargs, **kwargs)

        return make_response('Could not verify your credentials', 401, {'WWW-Authenticate': 'Basic realm="Login Realm"'})
    return login

parser = reqparse.RequestParser()
parser.add_argument('title')
parser.add_argument('year')

def abort_book_does_not_exist(book_id):
    if book_id not in BOOKS:
        abort(404, message='Book {} does not exist'.format(book_id))

class Book(Resource):
    def get(self, book_id):
        abort_book_does_not_exist(book_id)
        return BOOKS[book_id]
    
    @login_required
    def delete(self, book_id):
        abort_book_does_not_exist(book_id)
        del BOOKS[book_id]
        return '', 204
    
    def put(self, book_id):
        args = parser.parse_args()
        book_information = {'title' : args['title'], 'year': args['year']}
        BOOKS[book_id] = book_information
        return book_information, 201


class BookList(Resource):
    def get(self):
        return BOOKS
    def post(self):
        args = parser.parse_args()
        current_book_id = 0
        if len(BOOKS) > 0:
            for book in BOOKS:
                x = int(book.split('_')[-1])
                if x > current_book_id:
                    current_book_id = x
        
        BOOKS[f'book_{current_book_id + 1}'] = {'title': args['title'], 'year': args['year']}
        return BOOKS[f'book_{current_book_id + 1}'], 201
        
    
api.add_resource(Book, '/books/<book_id>')
api.add_resource(BookList, '/books')

if __name__ == '__main__':
    app.run(debug=True)