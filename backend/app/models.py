from datetime import datetime
from . import db

class Address(db.Model):
    __tablename__ = 'addresses'
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(255), nullable=False)

class Gender(db.Model):
    __tablename__ = 'genders'
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(50), nullable=False)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Boolean, default=True)
    admin = db.Column(db.Boolean, default=False)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    phone_number = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'))
    gender_id = db.Column(db.Integer, db.ForeignKey('genders.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    address = db.relationship('Address')
    gender = db.relationship('Gender')
    role = db.relationship('Role')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'role_id': self.role_id
        }

class State(db.Model):
    __tablename__ = 'states'
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean, default=True)
    archived = db.Column(db.Boolean, default=False)

class SurveyType(db.Model):
    __tablename__ = 'survey_types'
    id = db.Column(db.Integer, primary_key=True)
    customer_satisfaction = db.Column(db.Boolean)
    marketing = db.Column(db.Boolean)

class Survey(db.Model):
    __tablename__ = 'surveys'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    state_id = db.Column(db.Integer, db.ForeignKey('states.id'))
    created_by_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    survey_type_id = db.Column(db.Integer, db.ForeignKey('survey_types.id'))

    state = db.relationship('State')
    creator = db.relationship('User')
    survey_type = db.relationship('SurveyType')

    questions = db.relationship('Question', back_populates='survey', cascade='all, delete-orphan')


    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'created_at': self.created_at,
            'state_id': self.state_id,
            'created_by_id': self.created_by_id,
            'survey_type_id': self.survey_type_id
        }

class QuestionType(db.Model):
    __tablename__ = 'question_types'
    id = db.Column(db.Integer, primary_key=True)
    alternatives = db.Column(db.Boolean, default=False)
    essay_questions = db.Column(db.Boolean, default=False)

class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    
    survey_id = db.Column(db.Integer, db.ForeignKey('surveys.id'))
    question_type_id = db.Column(db.Integer, db.ForeignKey('question_types.id'))

    survey = db.relationship('Survey', back_populates='questions')
    responses = db.relationship('Response', back_populates='question', cascade='all, delete-orphan')
    question_type = db.relationship('QuestionType')

class Response(db.Model):
    __tablename__ = 'responses'
    id = db.Column(db.Integer, primary_key=True)
    response = db.Column(db.Text)
    response_choice = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    question = db.relationship('Question', back_populates='responses')
    user = db.relationship('User')
