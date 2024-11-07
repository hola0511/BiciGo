class Usuario:
    def __init__(self, id, nombre, correo, contrasena, rol):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        self.rol = rol

class Cliente(Usuario):
    def __init__(self, id, nombre, correo, contrasena):
        super().__init__(id, nombre, correo, contrasena, rol=False)

class Administrador(Usuario):
    def __init__(self, id, nombre, correo, contrasena):
        super().__init__(id, nombre, correo, contrasena, rol=True)