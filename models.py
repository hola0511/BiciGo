from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    correo = db.Column(db.String(150), unique=True, nullable=False)
    contraseña = db.Column(db.String(150), nullable=False)
    reservas = db.relationship('Reserva', backref='cliente', lazy=True)

class Estacion(db.Model):
    __tablename__ = 'estacion'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    ubicacion = db.Column(db.String(150), nullable=False)
    bicicletas = db.relationship('Bicicleta', backref='estacion', lazy=True)

class Bicicleta(db.Model):
    __tablename__ = 'bicicleta'
    id = db.Column(db.Integer, primary_key=True)
    estado = db.Column(db.Boolean, nullable=False, default=True)
    estacion_id = db.Column(db.Integer, db.ForeignKey('estacion.id'), nullable=False)

class Reserva(db.Model):
    __tablename__ = 'reserva'
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    estacion_id = db.Column(db.Integer, db.ForeignKey('estacion.id'), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    hora = db.Column(db.String(50), nullable=False)
    # Otros campos necesarios como distancia, duración, etc.
