# https://medium.com/python-pandemonium/build-simple-restful-api-with-python-and-flask-part-2-724ebf04d12

from flask import Flask, request
from flask_cors import CORS
import crud as crud

app = Flask(__name__)
CORS(app)


@app.route('/')
def health_check():
    return 'The server is working.'


@app.route('/quote/', methods=['GET'])
def get_quotes():
    return crud.get()


@app.route('/quote/<id>', methods=['GET'])
def get_quote(id):
    return crud.get_by_id(id)


@app.route('/quote/', methods=['POST'])
def create_quote():
    if request.method == 'POST':
        quote = request.get_json()
    return crud.create(quote)


@app.route('/quote/', methods=['PUT'])
def update_quote():
    if request.method == 'PUT':
        quote = request.get_json()
    return crud.update(quote)


@app.route('/quote/<id>', methods=['DELETE'])
def delete_quote(id):
    if request.method == 'DELETE':
        return crud.delete(id)


if __name__ == '__main__':
    # app.run()
    app.run(debug=True, port=3010)
