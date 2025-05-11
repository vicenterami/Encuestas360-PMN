from app import create_app, bcrypt
from app.models import db, User, Role, Gender, Address, SurveyType, State, Survey, QuestionType, Question, Response
from datetime import datetime

app = create_app()

with app.app_context():
    # Eliminar y crear todas las tablas
    db.drop_all()
    db.create_all()

    # Crear roles
    admin_role = Role(user=False, admin=True)
    user_role = Role(user=True, admin=False)
    db.session.add_all([admin_role, user_role])
    db.session.commit()

    # Crear géneros
    male = Gender(gender='Male')
    female = Gender(gender='Female')
    other = Gender(gender='Other')
    db.session.add_all([male, female, other])
    db.session.commit()

    # Crear direcciones
    address1 = Address(address='123 Main St')
    address2 = Address(address='456 Elm St')
    address3 = Address(address='789 Oak St')
    db.session.add_all([address1, address2, address3])
    db.session.commit()

    # Crear usuarios administradores (CON HASH)
    admin1 = User(
        name='Admin One',
        email='admin1@example.com',
        password=bcrypt.generate_password_hash('1234').decode('utf-8'),
        phone_number='1234567890',
        created_at=datetime.utcnow(),
        address_id=address1.id,
        gender_id=male.id,
        role_id=admin_role.id
    )
    admin2 = User(
        name='Admin Two',
        email='admin2@example.com',
        password=bcrypt.generate_password_hash('1234').decode('utf-8'),
        phone_number='0987654321',
        created_at=datetime.utcnow(),
        address_id=address2.id,
        gender_id=female.id,
        role_id=admin_role.id
    )
    db.session.add_all([admin1, admin2])
    db.session.commit()

    # Crear usuarios comunes (CON HASH)
    user1 = User(
        name='User One',
        email='user1@example.com',
        password=bcrypt.generate_password_hash('abcd').decode('utf-8'),
        phone_number='1112223333',
        created_at=datetime.utcnow(),
        address_id=address3.id,
        gender_id=other.id,
        role_id=user_role.id
    )
    user2 = User(
        name='User Two',
        email='user2@example.com',
        password=bcrypt.generate_password_hash('abcd').decode('utf-8'),
        phone_number='4445556666',
        created_at=datetime.utcnow(),
        address_id=address1.id,
        gender_id=male.id,
        role_id=user_role.id
    )
    db.session.add_all([user1, user2])
    db.session.commit()

    # Crear tipos de encuesta
    customer_satisfaction = SurveyType(customer_satisfaction=True, marketing=False)
    marketing = SurveyType(customer_satisfaction=False, marketing=True)
    db.session.add_all([customer_satisfaction, marketing])
    db.session.commit()

    # Crear estados de encuesta
    active_state = State(active=True, archived=False)
    archived_state = State(active=False, archived=True)
    db.session.add_all([active_state, archived_state])
    db.session.commit()

    # Crear encuestas
    survey1 = Survey(
        title='Customer Feedback',
        description='Survey about customer satisfaction.',
        created_at=datetime.utcnow(),
        state_id=active_state.id,
        created_by_id=admin1.id,
        survey_type_id=customer_satisfaction.id
    )
    survey2 = Survey(
        title='Market Research',
        description='Survey about market trends.',
        created_at=datetime.utcnow(),
        state_id=archived_state.id,
        created_by_id=admin2.id,
        survey_type_id=marketing.id
    )
    db.session.add_all([survey1, survey2])
    db.session.commit()

    # Crear tipos de pregunta
    multiple_choice = QuestionType(alternatives=True, essay_questions=False)
    open_ended = QuestionType(alternatives=False, essay_questions=True)
    db.session.add_all([multiple_choice, open_ended])
    db.session.commit()

    # Crear preguntas
    question1 = Question(
        question='How satisfied are you with our service?',
        survey_id=survey1.id,
        question_type_id=multiple_choice.id
    )
    question2 = Question(
        question='What can we improve?',
        survey_id=survey1.id,
        question_type_id=open_ended.id
    )
    question3 = Question(
        question='Which products do you prefer?',
        survey_id=survey2.id,
        question_type_id=multiple_choice.id
    )
    db.session.add_all([question1, question2, question3])
    db.session.commit()

    # Crear respuestas
    response1 = Response(
        response='Very satisfied',
        response_choice=5,
        created_at=datetime.utcnow(),
        question_id=question1.id,
        user_id=user1.id
    )
    response2 = Response(
        response='Improve customer support.',
        response_choice=None,
        created_at=datetime.utcnow(),
        question_id=question2.id,
        user_id=user1.id
    )
    response3 = Response(
        response='Product A',
        response_choice=1,
        created_at=datetime.utcnow(),
        question_id=question3.id,
        user_id=user2.id
    )
    db.session.add_all([response1, response2, response3])
    db.session.commit()

    print("✅ Base de datos inicializada con datos de prueba.")
