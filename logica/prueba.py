import sqlite3
from datetime import datetime

# Clase Usuario
class Usuario:
    def __init__(self, nombre, correo, contrasena, rol):
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        self.rol = rol

# Clase Cliente, que hereda de Usuario
class Cliente(Usuario):
    def __init__(self, nombre, correo, contrasena):
        super().__init__(nombre, correo, contrasena, rol=False)
        self.historial = []

# Clase Administrador, que hereda de Usuario
class Administrador(Usuario):
    def __init__(self, nombre, correo, contrasena):
        super().__init__(nombre, correo, contrasena, rol=True)

# Clase GestorUsuarios para gestionar usuarios
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
                    return Administrador(user[1], user[2], user[3])
            else:
                cursor.execute("SELECT * FROM Cliente WHERE correo = ? AND contrasena = ?", (correo, contrasena))
                user = cursor.fetchone()
                if user:
                    print("Inicio de sesión exitoso como cliente.")
                    return Cliente(user[1], user[2], user[3])
            print("Credenciales incorrectas.")
            return None

# Clase Estacion
class Estacion:
    def __init__(self, id, numero_bicicletas):
        self.id = id
        self.numero_bicicletas = numero_bicicletas

# Clase GestorEstacion para manejar estaciones
class GestorEstacion:
    @staticmethod
    def agregar_estacion(nombre, ubicacion, id_administrador):
        with sqlite3.connect('base_de_datos.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Estacion (nombre, ubicacion, id_administrador) VALUES (?, ?, ?)",
                           (nombre, ubicacion, id_administrador))
            conn.commit()
            print("Estación agregada exitosamente.")

    @staticmethod
    def editar_estacion(id_estacion, nombre, ubicacion):
        with sqlite3.connect('base_de_datos.db') as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE Estacion SET nombre = ?, ubicacion = ? WHERE id = ?",
                           (nombre, ubicacion, id_estacion))
            conn.commit()
            print("Estación editada exitosamente.")

    @staticmethod
    def eliminar_estacion(id_estacion):
        with sqlite3.connect('base_de_datos.db') as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Estacion WHERE id = ?", (id_estacion,))
            conn.commit()
            print("Estación eliminada exitosamente.")

# Clase Bicicleta
class Bicicleta:
    def __init__(self, estado):
        self.estado = estado

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

# Clase Queja
class Queja:
    def __init__(self, cliente, razon, estado):
        self.cliente = cliente
        self.razon = razon
        self.estado = estado

# Clase GestorCliente para manejar quejas e historial
class GestorCliente:
    @staticmethod
    def crear_queja(cliente_id, razon):
        with sqlite3.connect('base_de_datos.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Queja (id_cliente, razon, estado) VALUES (?, ?, ?)", (cliente_id, razon, False))
            conn.commit()
            print("Queja registrada exitosamente.")

    @staticmethod
    def consultar_historial(cliente_id):
        with sqlite3.connect('base_de_datos.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Reserva WHERE id_cliente = ?", (cliente_id,))
            reservas = cursor.fetchall()
            print("Historial de reservas:")
            for reserva in reservas:
                print(reserva)

# Clase Reserva
class Reserva:
    def __init__(self, fecha, distancia, duracion, hora):
        self.fecha = fecha
        self.distancia = distancia
        self.duracion = duracion
        self.hora = hora

# Clase GestorReserva para manejar reservas
class GestorReserva:
    @staticmethod
    def crear_reserva(cliente_id, estacion_id, distancia_id):
        fecha = datetime.now().strftime('%Y-%m-%d')
        hora = datetime.now().strftime('%H:%M:%S')
        with sqlite3.connect('base_de_datos.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Reserva (fecha, hora, id_cliente, id_estacion, id_distancia) VALUES (?, ?, ?, ?, ?)",
                           (fecha, hora, cliente_id, estacion_id, distancia_id))
            conn.commit()
            print("Reserva creada exitosamente.")

    @staticmethod
    def eliminar_reserva(reserva_id):
        with sqlite3.connect('base_de_datos.db') as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Reserva WHERE id = ?", (reserva_id,))
            conn.commit()
            print("Reserva eliminada exitosamente.")

# Clase Notificacion para manejar alertas
class Notificacion:
    @staticmethod
    def enviar_notificacion(cliente_id, mensaje):
        print(f"Notificación para el cliente {cliente_id}: {mensaje}")
