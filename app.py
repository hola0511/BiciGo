from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config
from models import db, Cliente, Administrador, Estacion, Bicicleta, Queja, Reserva, Distancia
from forms import RegisterForm, LoginForm

# Inicialización de la aplicación
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Configuración de Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return Cliente.query.get(int(user_id))  # Asume que solo los clientes inician sesión

# Ruta de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Registro de clientes
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.contraseña.data, method='sha256')
        new_user = Cliente(nombre=form.nombre.data, correo=form.correo.data, contraseña=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Usuario registrado exitosamente.')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

# Inicio de sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Cliente.query.filter_by(correo=form.correo.data).first()
        if user and check_password_hash(user.contraseña, form.contraseña.data):
            login_user(user)
            return redirect(url_for('index'))
        flash('Correo o contraseña incorrectos')
    return render_template('login.html', form=form)

# Cerrar sesión
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# Rutas para gestionar estaciones (para administradores)
@app.route('/admin/estaciones', methods=['GET', 'POST'])
@login_required
def gestionar_estaciones():
    if not current_user.is_authenticated or not isinstance(current_user, Administrador):
        flash("Acceso denegado")
        return redirect(url_for('index'))

    if request.method == 'POST':
        nombre = request.form.get('nombre')
        ubicacion = request.form.get('ubicacion')
        nueva_estacion = Estacion(id_administrador=current_user.id, nombre=nombre, ubicacion=ubicacion)
        db.session.add(nueva_estacion)
        db.session.commit()
        flash("Estación añadida exitosamente")

    estaciones = Estacion.query.all()
    return render_template('admin/estaciones.html', estaciones=estaciones)

# Reserva de bicicletas
@app.route('/reservar', methods=['GET', 'POST'])
@login_required
def reservar():
    estaciones = Estacion.query.all()
    if request.method == 'POST':
        estacion_id = request.form.get('estacion_id')
        fecha = request.form.get('fecha')
        hora = request.form.get('hora')
        nueva_reserva = Reserva(id_cliente=current_user.id, id_estacion=estacion_id, fecha=fecha, hora=hora)
        db.session.add(nueva_reserva)
        db.session.commit()
        flash("Reserva realizada exitosamente")
        return redirect(url_for('index'))
    return render_template('reservar.html', estaciones=estaciones)

# Historial de reservas de clientes
@app.route('/historial')
@login_required
def historial():
    reservas = Reserva.query.filter_by(id_cliente=current_user.id).all()
    return render_template('historial.html', reservas=reservas)

# Creación de tablas en la base de datos
with app.app_context():
    db.create_all()

    if not Cliente.query.first():  # Solo agrega registros si la tabla Cliente está vacía
        # Crear un cliente de prueba
        nuevo_cliente = Cliente(nombre="Juan Pérez", correo="juan@example.com", contraseña="password123")
        db.session.add(nuevo_cliente)

        # Crear un administrador de prueba y guardar en la base de datos
        nuevo_admin = Administrador(nombre="Admin Uno", correo="admin@example.com", contraseña="adminpassword")
        db.session.add(nuevo_admin)
        db.session.commit()  # Guarda el administrador para que tenga un ID asignado

        # Crear una estación de prueba, utilizando el ID del administrador recién creado
        nueva_estacion = Estacion(id_administrador=nuevo_admin.id, nombre="Estación Centro",
                                  ubicacion="Centro de la Ciudad")
        db.session.add(nueva_estacion)

        # Guardar cambios en la base de datos
        db.session.commit()
        print("Registros de prueba añadidos a la base de datos.")
    else:
        print("Los registros de prueba ya existen en la base de datos.")

    clientes = Cliente.query.all()
    administradores = Administrador.query.all()
    estaciones = Estacion.query.all()

    print("Clientes guardados en la base de datos:")
    for cliente in clientes:
        print(f"ID: {cliente.id}, Nombre: {cliente.nombre}, Correo: {cliente.correo}")

    print("\nAdministradores guardados en la base de datos:")
    for admin in administradores:
        print(f"ID: {admin.id}, Nombre: {admin.nombre}, Correo: {admin.correo}")

    print("\nEstaciones guardadas en la base de datos:")
    for estacion in estaciones:
        print(
            f"ID: {estacion.id}, Nombre: {estacion.nombre}, Ubicación: {estacion.ubicacion}, ID Administrador: {estacion.id_administrador}")

if __name__ == '__main__':
    app.run(debug=True)
