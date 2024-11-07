import sqlite3
from .usuario import Cliente, Administrador

class GestorUsuarios:
    @staticmethod
    def registrar_usuario(nombre, correo, contrasena, rol):
        with sqlite3.connect('base_de_datos.db') as conn:
            cursor = conn.cursor()
            if rol:
                cursor.execute("INSERT INTO Administrador (nombre, correo, contrasena) VALUES (?, ?, ?)",
                               (nombre, correo, contrasena))
            else:
                cursor.execute("INSERT INTO Cliente (nombre, correo, contrasena) VALUES (?, ?, ?)",
                               (nombre, correo, contrasena))
            conn.commit()
            print("Usuario registrado exitosamente.")

    @staticmethod
    def login_usuario(correo, contrasena, rol):
        with sqlite3.connect('base_de_datos.db') as conn:
            cursor = conn.cursor()
            if rol:
                cursor.execute("SELECT * FROM Administrador WHERE correo = ? AND contrasena = ?", (correo, contrasena))
                user = cursor.fetchone()
                if user:
                    print("Inicio de sesión exitoso como administrador.")
                    return Administrador(user[0], user[1], user[2], user[3])
            else:
                cursor.execute("SELECT * FROM Cliente WHERE correo = ? AND contrasena = ?", (correo, contrasena))
                user = cursor.fetchone()
                if user:
                    print("Inicio de sesión exitoso como cliente.")
                    return Cliente(user[0], user[1], user[2], user[3])
            print("Credenciales incorrectas.")
            return None