from app import create_app
from app.models import db, User

app = create_app()

with app.app_context():
    # Limpia base si ya existía algo (opcional)
    db.drop_all()
    db.create_all()

    # Crear datos de prueba
    usuarios = [
        User(name="Ana González", email="ana@correo.com", password="1234"),
        User(name="Luis Pérez", email="luis@correo.com", password="abcd"),
        User(name="Claudia Ruiz", email="claudia@correo.com", password="admin"),
        User(name="Vicente", email="vramirez2020@alu.uct.cl", password="abcd")
    ]

    db.session.add_all(usuarios)
    db.session.commit()
    print("✅ Base de datos inicializada con datos de prueba.")
