# FIRST FLASK API

This app contains 5 books (titles and release date) from Brazilian romance writer: Machado de Assis
and provide a API to Get, Update, Post and Delete books from the list in runtime.


## API commands usage

### GET
Get all 5 books from the app.

GET - `http://127.0.0.1:5000/books`

Returns:
`{
    "book_1": {
        "title": "Dom Casmurro",
        "year": "1899"
    },
    "book_2": {
        "title": "The Posthumous Memoris of Bras Cubas",
        "year": "1881"
    },
    "book_3": {
        "title": "The Fortune-Teller",
        "year": "1884"
    },
    "book_4": {
        "title": "Quincas Borba",
        "year": "1891"
    },
    "book_5": {
        "title": "O alienista",
        "year": "1882"
    }
}`

Get specific book by providing ID.

GET - `http://127.0.0.1:5000/books/book_1`

Returns:
`{
    "title": "Dom Casmurro",
    "year": "1899"
}`

### POST
Append an book to the list (at the end).

POST - `http://127.0.0.1:5000/books`

BODY - `{
    "title": "Old House",
    "year": "1886"
}`

### PUT
Allow to add an book providing an ID at the end of URL.

PUT - `http://127.0.0.1:5000/books/book_6`

BODY - `{
    "title": "Old House",
    "year": "1886"
}`

### DELETE
Delete book from specific index(ID).

OBS: requires authentication (using Basic Auth as Username: machado and deassis123)

DELETE - `http://127.0.0.1:5000/books/book_3`


## Requirements
<img src="https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/Python-Dark.svg" width="25" height=25> - Python 3.11.0

<img src="https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/Flask-Dark.svg" width="25" height=25> - Flask 3.0.2 and Flask Restful 0.3.10


## Credits
Based in Udemy's course: "Application Programming Interface: API and Web Services"
Credits to: [Eric Roby](https://github.com/codingwithroby)
