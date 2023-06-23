"""
FLASK_ENV: Der Name der aktuellen Serverumgebung (z.B. 'dev' oder 'prod').
SECRET_KEY: Ein Geheimnis, das verwendet wird, um die Daten des Servers zu signieren und zu sichern.
SERVER_HOST: Der Hostname oder die IP-Adresse, auf der der Server lauscht.
SERVER_PORT: Der Port, auf dem der Server lauscht.
DB_HOST: Der Hostname oder die IP-Adresse der Datenbank, auf die zugegriffen werden soll.
DB_PORT: Der Port der Datenbank.
DB_NAME: Der Name der Datenbank.
DB_USERNAME und DB_PASSWORD: Die Anmeldeinformationen, um die Verbindung zur Datenbank herzustellen.
AUTH_SECRET: Ein Geheimnis, das zur Verschlüsselung von JWTs verwendet wird.
AUTH_EXPIRATION: Die Dauer in Sekunden, für die JWTs gültig sind.
CACHE_TYPE: Der Typ des Caching-Systems (z.B. 'simple' oder 'redis').
CACHE_DEFAULT_TIMEOUT: die Standard-Timeout-Zeit für das Caching-System.

"""

import os

# Flask configurations
FLASK_ENV = os.environ.get('FLASK_ENV', 'dev')
SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')
JSON_SORT_KEYS = False
APP_DEBUG = True

# Server configurations
SERVER_HOST = os.environ.get('SERVER_HOST', 'localhost')
SERVER_PORT = int(os.environ.get('SERVER_PORT', 5000))

# Database configurations
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = int(os.environ.get('DB_PORT', 27017))
DB_NAME = os.environ.get('DB_NAME', 'ai_author')
DB_USERNAME = os.environ.get('DB_USERNAME', 'root')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'default_password')

# Auth configurations
AUTH_SECRET = os.environ.get('AUTH_SECRET', 'default_auth_secret')
AUTH_EXPIRATION = 600

# Cache configurations
CACHE_TYPE = os.environ.get('CACHE_TYPE', 'simple')
CACHE_DEFAULT_TIMEOUT = int(os.environ.get('CACHE_TIMEOUT', 300))
