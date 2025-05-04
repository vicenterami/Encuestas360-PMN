# backend/venv/app/routes.py
from flask import Blueprint, jsonify, request
from .models import db, User


main = Blueprint('main', __name__)

# Simulación de base de datos
users = []

@main.route('/')
def index():
    return jsonify({"message": "Backend funcionando"})

@main.route('/register', methods=['POST'])
def register():
    data = request.json
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"success": False, "message": "Correo ya registrado"}), 409

    new_user = User(name=data['name'], email=data['email'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"success": True, "message": "Usuario registrado exitosamente"})

@main.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email'], password=data['password']).first()

    if user:
        return jsonify({"success": True, "message": "Inicio de sesión exitoso", "user": user.to_dict()})
    return jsonify({"success": False, "message": "Credenciales inválidas"}), 401


@main.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = User.query.all()
    return jsonify([u.to_dict() for u in usuarios])
