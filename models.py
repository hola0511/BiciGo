from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cliente(db.Model):
    __tablename__ = 'cliente'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    correo = db.Column(db.String, unique=True, nullable=False)
    contraseña = db.Column(db.String, nullable=False)
    reservas = db.relationship('Reserva', backref='cliente', lazy=True)
    quejas = db.relationship('Queja', backref='cliente', lazy=True)


class Administrador(db.Model):
    __tablename__ = 'administrador'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    correo = db.Column(db.String, unique=True, nullable=False)
    contraseña = db.Column(db.String, nullable=False)
    estaciones = db.relationship('Estacion', backref='administrador', lazy=True)


class Estacion(db.Model):
    __tablename__ = 'estacion'
    id = db.Column(db.Integer, primary_key=True)
    id_administrador = db.Column(db.Integer, db.ForeignKey('administrador.id'), nullable=False)
    nombre = db.Column(db.String, nullable=False)
    ubicacion = db.Column(db.String, nullable=False)
    bicicletas = db.relationship('Bicicleta', backref='estacion', lazy=True)
    reservas = db.relationship('Reserva', backref='estacion', lazy=True)


class Bicicleta(db.Model):
    __tablename__ = 'bicicleta'
    id = db.Column(db.Integer, primary_key=True)
    estado = db.Column(db.Boolean, nullable=False, default=True)
    id_estacion = db.Column(db.Integer, db.ForeignKey('estacion.id'), nullable=False)


class Queja(db.Model):
    __tablename__ = 'queja'
    id = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    razon = db.Column(db.String, nullable=False)
    estado = db.Column(db.Boolean, default=True)
    id_estacion = db.Column(db.Integer, db.ForeignKey('estacion.id'), nullable=True)


class Reserva(db.Model):
    __tablename__ = 'reserva'
    id = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    id_estacion = db.Column(db.Integer, db.ForeignKey('estacion.id'), nullable=False)
    fecha = db.Column(db.String, nullable=False)
    hora = db.Column(db.String, nullable=False)
    id_distancia = db.Column(db.Integer, db.ForeignKey('distancia.id'), nullable=True)


class Distancia(db.Model):
    __tablename__ = 'distancia'
    id = db.Column(db.Integer, primary_key=True)
    distancia = db.Column(db.String, nullable=False)
    id_estacion_inicio = db.Column(db.Integer, db.ForeignKey('estacion.id'), nullable=False)
    id_estacion_llegada = db.Column(db.Integer, db.ForeignKey('estacion.id'), nullable=False)
    tiempo = db.Column(db.String, nullable=False)
