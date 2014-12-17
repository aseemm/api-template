from flask import render_template, flash, redirect, session, url_for, request, \
    g, jsonify
from flask.ext.sqlalchemy import get_debug_queries
from app import app, db
from .models import Book
from config import DATABASE_QUERY_TIMEOUT

@app.route('/books', methods=['GET'])
def list_books():
    if request.method == 'GET':
        lim = request.args.get('limit', 2)
        off = request.args.get('offset', 0)

        results = Book.query.limit(lim).offset(off).all()

        json_results = []
        for result in results:
            d = {'id': result.id,
                 'title': result.title,
                 'author': result.author,
                 'link': result.link}
            json_results.append(d)
            
        return jsonify(items=json_results)

@app.route('/books/<int:book_id>', methods=['GET'])
def list_book(book_id):
    if request.method == 'GET':
        result = Book.query.filter_by(id=book_id).first()

    json_result = {'id': result.id,
                   'title': result.title,
                   'author': result.author,
                   'link': result.link}

    return jsonify(items=json_result)

@app.route('/books', methods=['POST'])
def create_book():
    if not request.json or not 'title' in request.json:
        abort(400)

    book = Book(title=request.json['title'], author=request.json['author'], link=request.json.get('link', ""))
    db.session.add(book)
    db.session.commit()

    json_result = {'title': book.title,
                   'author': book.author,
                   'link': book.link}

    return jsonify(items=json_result)

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    if request.method == 'PUT':
        book = Book.query.filter_by(id=book_id).first()

        book.title = request.json.get('title', book.title)
        book.author = request.json.get('author', book.author)
        book.link = request.json.get('link', book.link)
    
        db.session.add(book)
        db.session.commit()

        json_result = {'id': book.id,
                       'title': book.title,
                       'author': book.author,
                       'link': book.link}

        return jsonify(items=json_result)

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    if request.method == 'DELETE':
        book = Book.query.filter_by(id=book_id).first()
        db.session.delete(book)
        db.session.commit()

        return jsonify({'result': True})


# curl -i http://localhost:5000/books?limit=10
# curl -i -H "Content-Type: application/json" -X POST -d '{"title":"D", "author":"D"}' http://localhost:5000/books
# curl -i -H "Content-Type: application/json" -X PUT -d '{"title":"Darva"}' http://localhost:5000/books/11
# curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/books/11
