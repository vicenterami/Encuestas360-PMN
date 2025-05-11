from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
import os
from dotenv import load_dotenv
from flask_migrate import Migrate

migrate = Migrate()
bcrypt = Bcrypt()
jwt = JWTManager()
db = SQLAlchemy()  # ✔️ Mantener fuera si usas modelos en otros archivos

def create_app():
    app = Flask(__name__)
    load_dotenv()

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")

    CORS(app)
    # Inicializa las extensiones con la app
    bcrypt.init_app(app) 
    db.init_app(app)  # ✔️ Ahora db se inicializa dentro de create_app
    jwt.init_app(app)
    migrate.init_app(app, db)

    # Importa los modelos y rutas dentro del contexto para evitar problemas
    with app.app_context():
        db.create_all()
        from .routes import main  # ✔️ Importar aquí si hay dependencias circulares
        app.register_blueprint(main, url_prefix='/api')

    return app