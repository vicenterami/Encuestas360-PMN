from flask import Blueprint, jsonify, request
from . import bcrypt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from .models import db, User, Role, Survey
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return jsonify({"message": "Backend funcionando"})

@main.route('/register', methods=['POST'])
def register():
    data = request.json
    existing_user = User.query.filter_by(email=data['email']).first()
    if existing_user:
        return jsonify({"success": False, "message": "Correo ya registrado"}), 409

    user_role = Role.query.filter_by(user=True).first()
    if not user_role:
        return jsonify({"success": False, "message": "Rol de usuario no definido"}), 500

    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

    new_user = User(
        name=data['name'],
        email=data['email'],
        password=hashed_password,
        phone_number=data.get('phone_number') or None,
        created_at=datetime.utcnow(),
        address_id=data.get('address_id') or None,
        gender_id=data.get('gender_id') or None,
        role_id=user_role.id
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"success": True, "message": "Usuario registrado exitosamente"})

@main.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()

    if user and bcrypt.check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=user.id)
        # Agregar información del usuario (incluyendo si es admin)
        return jsonify({
            "success": True,
            "access_token": access_token,
            "is_admin": user.role.admin  # <-- Clave faltante
        }), 200

    return jsonify({"success": False, "message": "Credenciales inválidas"}), 401

@main.route('/usuarios', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])


@main.route('/surveys', methods=['POST'])
@jwt_required()
def create_survey():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    if not user or not user.role.admin:
        return jsonify({"success": False, "message": "No autorizado"}), 403

    data = request.json
    title = data.get('title')
    description = data.get('description')

    if not title:
        return jsonify({"success": False, "message": "El título es obligatorio"}), 400

    new_survey = Survey(
        title=title,
        description=description,
        created_at=datetime.utcnow(),
        created_by_id=user.id,
        state_id=1,  # Estado por defecto
        survey_type_id=data.get('survey_type_id') or None
    )
    db.session.add(new_survey)
    db.session.commit()

    return jsonify({"success": True, "message": "Encuesta creada exitosamente"})
  