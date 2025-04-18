from flask import Blueprint, jsonify, request

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return jsonify({"message": "Backend funcionando"})

@main.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    # validar (falso por ahora)
    return jsonify({"success": username == "admin" and password == "123"})
