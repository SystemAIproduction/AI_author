import os
import unittest
from api.user_authentication.user_authentication_service import app, mongodb
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps

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


class TestUserInterface(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Einen Testbenutzer in die Datenbank einfügen
        hashed_password = generate_password_hash('password', method='sha256')
        user = {'username': 'max.mustermann', 'password': hashed_password, 'email': 'max.mustermann@example.com'}
        mongodb.users.insert_one(user)
        
    @classmethod
    def tearDownClass(cls):
        # Den Testbenutzer aus der Datenbank entfernen
        mongodb.users.delete_one({'username': 'max.mustermann'})
        
    def test_register(self):
        # Teste die Registrierungsfunktion mit einem bereits registrierten Benutzer
        response = app.test_client().post('/register', json={'username': 'max.mustermann', 'password': 'password', 'email': 'max.mustermann@example.com'})
        self.assertEqual(response.status_code, 409)
        
        # Teste die Registrierungsfunktion mit einem neuen Benutzer
        response = app.test_client().post('/register', json={'username': 'anna.mustermann', 'password': 'password', 'email': 'anna.mustermann@example.com'})
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'User created successfully!', response.data)
        
    def test_login(self):
        # Teste die Anmeldungsfunktion mit einem gültigen Benutzer
        response = app.test_client().get('/login', headers={'Authorization': 'Basic bWF4Lm11c3Rlcm1hbm46cGFzc3dvcmQ='})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'token', response.data)
        
        # Teste die Anmeldungsfunktion mit einem ungültigen Benutzer
        response = app.test_client().get('/login', headers={'Authorization': 'Basic dGVzdC11c2VyOnBhc3N3b3Jk'})
        self.assertEqual(response.status_code, 401)
        self.assertIn(b'Could not verify!', response.data)

        
if __name__ == '__main__':
    unittest.main(argv=[os.path.abspath(__file__)])
