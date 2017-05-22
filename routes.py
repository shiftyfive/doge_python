import sqllite3
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/doggos', methods=['GET', 'POST'])
def collecion():
    if request.method == 'GET'
        pass # Handle GET all Request
    elif request.method == 'POST':
        data = request.form
        result = add_song(data['name'], data['breed'], data['rating'])
        return jsonify(result)

@app.route('/api/doggos/<doggo_id>', methods=['GET', 'PUT', 'DELETE'])
def resources(song_id):
    if request.method == 'GET':
        pass # Handle GET single request
    elif request.method == 'PUT':
        pass # Handle UPDATE request
    elif request.method == 'DELETE':
        pass #Handle DELETE request


# seed functions there is no better place to put this.

def add_doggo(name, breed, rating):
    try:
        with sqlite3.connect('doges.db') as connection:
            cursor = connection.cursor()
            cursor.execute("""
            INSERT INTO doggos (name, breed, rating) values (?, ?, ?);
            """, (name, breed, rating))
        result = {'status': 1, 'message': 'pupper added'}
    except:
        result = {'status': 0, 'message': 'error'}
    return result
