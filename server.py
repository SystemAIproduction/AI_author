from flask import Flask, request, jsonify
from api.user_authentication.user_authentication_service import user_auth_bp
from api.content_management.content_management_service import content_mgmt_bp
from api.text_generation.text_generation_service import text_gen_bp
from api.information_source.information_source_service import info_src_bp
from api.user_interface.user_interface_service import user_intf_bp
from api.rating.rating_service import rating_bp
from config.server_config import SERVER_HOST, SERVER_PORT

app = Flask(__name__)

# Blueprints for the different services
app.register_blueprint(user_auth_bp, url_prefix='/user-auth')
app.register_blueprint(content_mgmt_bp, url_prefix='/content-mgmt')
app.register_blueprint(text_gen_bp, url_prefix='/text-gen')
app.register_blueprint(info_src_bp, url_prefix='/info-src')
app.register_blueprint(user_intf_bp, url_prefix='/user-intf')
app.register_blueprint(rating_bp, url_prefix='/rating')

# Default route
@app.route('/')
def index():
    return "Welcome to the AI-Author API"

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "404: Not Found"})

if __name__ == '__main__':
    app.run(host=SERVER_HOST, port=SERVER_PORT)
