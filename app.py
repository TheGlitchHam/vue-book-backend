from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid
import db


# conf
DEBUG = True

# app instance
app = Flask(__name__)
app.config.from_object(__name__)

# enable cors
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check


@app.route("/ping", methods=['GET'])
def ping_pong():
    return jsonify("pong!")


@app.route("/books", methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == "POST":
        post_data = request.get_json()

        response_object['message'] = db.add_book_db({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
    else:
        response_object['books'] = db.get_all_books()
    return jsonify(response_object)


@app.route("/books/<book_id>", methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        response_object['message'] = db.update_book({
            'id': book_id,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
    if request.method == 'DELETE':
        response_object['message'] = db.delete_book(book_id)
    return jsonify(response_object)


if __name__ == "__main__":
    app.run()
