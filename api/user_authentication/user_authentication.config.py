import os

# Konfiguration für MongoDB
MONGO_URI = os.environ.get('MONGODB_URI')

# Konfiguration für JWT
SECRET_KEY = os.environ.get('SECRET_KEY')
