from flask import Flask
from flask_cors import CORS
from .models import db
from .routes import main
import os
from dotenv import load_dotenv

load_dotenv() # Cargar variables de entorno desde el archivo .env

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    CORS(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(main, url_prefix='/api')
    return app
