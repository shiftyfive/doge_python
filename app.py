import sqlite3
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/doggos', methods=['GET', 'POST'])
def collecion():
    if request.method == 'GET':
        all_doggos = get_all_doggos()
        return json.dumps(all_doggos)
    elif request.method == 'POST':
        data = request.form
        result = add_doggo(data['name'], data['breed'], data['rating'])
        return jsonify(result)

@app.route('/api/doggos/<doggo_id>', methods=['GET', 'PUT', 'DELETE'])
def resources(song_id):
    if request.method == 'GET':
        doggo = get_single_doggo(doggo_id)
        return json.dumps(doggo)
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

def get_all_doggos():
    with sqlite3.connect('doges.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM songs ORDER BY id desc")
        all_doggos = cursor.fetchall()
        return all_doggos

def get_single_doggo(dog_id):
    with sqlite3.connect('songs.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM doggos WHERE id = ?", (dog_id,))
        song = cursor.fetchone()
        return song

def edit_doggo(doggo_id, name, breed, rating):
    try:
        with sqlite3.connect(doges.db) as connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE doggos SET name = ?, breed = ? WHERE ID = ?;", (name, breed, rating, doggo_id))
            result = {'status': 1, 'message': 'Pupper Edited'}
        except:
            result = {'status': 0, 'message': 'Error'}
        return result

def delete_doggo(doggo_id):
    try:
        with sqlite3.connect(doges.db) as connection:
            cursor.execute("DELETE FROM doggos WHERE ID = ?;", (doggo_id))
            result = {'status': 1, 'message': 'Pupper deleted :('}
        except:
            result = {'status': 0, 'message': 'Error'}
        return result

if __name__ == '__main__':
    app.debug = True
    app.run()
