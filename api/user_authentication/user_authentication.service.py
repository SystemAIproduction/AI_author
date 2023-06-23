from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps
from app import app, mongodb

# JWT-Authentifizierungsfunktion
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = mongodb.users.find_one({'username': data['username']})
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        return f(current_user, *args, **kwargs)
    return decorated

# Benutzerregistrierungsfunktion
@app.route('/register', methods=['POST'])
def register_user():
    username = request.json['username']
    password = request.json['password']
    hashed_password = generate_password_hash(password, method='sha256')
    email = request.json['email']
    # Überprüfen, ob der Benutzer bereits registriert ist
    if not mongodb.users.find_one({'username': username}):
        user = {'username': username, 'password': hashed_password, 'email': email}
        mongodb.users.insert_one(user)
        return jsonify({'message': 'User created successfully!'}), 201
    else:
        return jsonify({'message': 'User already exists!'}), 409

# Benutzerloginfunktion
@app.route('/login')
def login_user():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'Could not verify!'}), 401
    user = mongodb.users.find_one({'username': auth.username})
    if not user:
        return jsonify({'message': 'Could not verify!'}), 401
    if check_password_hash(user['password'], auth.password):
        token = jwt.encode({'username': user['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'token': token}), 200
    return jsonify({'message': 'Could not verify!'}), 401
