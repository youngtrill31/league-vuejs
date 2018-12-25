from flask import Flask, json, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import (create_access_token)

#instatiate app
app = Flask(__name__)

# Enable CORS
CORS(app)

app.config['MONGO_DBNAME'] = 'jdleague'
app.config['MONGO_URI'] = 'mongodb://jdeleon:gamebang08@ds123434.mlab.com:23434/jdleague'
app.config['JWT_SECRET_KEY'] = 'secret'

mongo = PyMongo(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

@app.route('/team_registration', methods=['POST'])
def team_registration():
    teams = mongo.db.teams
    team_name = request.get_json()['team_name']
    manager_name = request.get_json()['manager_name']
    manager_email = request.get_json()['manager_email']
    password = bcrypt.generate_password_hash(request.get_json()['password']).decode('utf-8')
    created = datetime.now()
    location = request.get_json()['selected_location']
    division = request.get_json()['selected_division']

    team_id = teams.insert({
        'team_name': team_name,
        'manager_name': manager_name,
        'manager_email': manager_email,
        'password': password,
        'created': created,
        'roster': [],
        'location': location,
        'division': division,
    })

    new_team = teams.find_one({'_id': team_id})

    result = {'Team ' : new_team['team_name'] + ' registered'}

    return jsonify({'result' : result})

@app.route('/team_login', methods=['POST'])
def team_login():
    team = mongo.db.teams
    manager_email = request.get_json()['manager_email']
    password = request.get_json()['password']
    result = ''

    response = team.find_one({'manager_email': manager_email})

    if response:
        if bcrypt.check_password_hash(response['password'], password):
            access_token = create_access_token(identity= {
                'manager_email': response['manager_email']
            })
            result = jsonify({'token': access_token})
        else:
            result = jsonify({'error': 'Invalid username and password'})
    else:
        result = jsonify({'result': 'No results found'})

    return result

@app.route('/teams')
def teams():
    team = mongo.db.teams
    cursor = team.find({})
    team_list = []

    for doc in cursor:
        team_list.append(doc['team_name'])

    return jsonify(team_list)

@app.route('/locations')
def locations():
    locations = mongo.db.locations
    cursor = locations.find({})
    locations_list = []

    for doc in cursor:
        locations_list.append(doc['city'])

    return jsonify(locations_list)

@app.route('/divisions')
def divisions():
    divisions = mongo.db.divisions
    cursor = divisions.find({})
    divisions_list = []

    for doc in cursor:
        divisions_list.append(doc['name'])

    return jsonify(divisions_list)


if __name__ == 'main':
    app.run()