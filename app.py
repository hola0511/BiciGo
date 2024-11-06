from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required
from models import db, User, Estacion, Bicicleta, Reserva
from forms import RegisterForm, LoginForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(nombre=form.nombre.data, correo=form.correo.data, contraseña=form.contraseña.data)
        db.session.add(user)
        db.session.commit()
        flash('Usuario registrado exitosamente.')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(correo=form.correo.data).first()
        if user and user.check_password(form.contraseña.data):
            login_user(user)
            return redirect(url_for('index'))
        flash('Correo o contraseña incorrectos')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# Aquí añadimos otras rutas para la reserva, gestión de estaciones, etc.

if __name__ == '__main__':
    app.run(debug=True)
