import sqlite3

class GestorEstacion:
    @staticmethod
    def agregar_estacion(nombre, ubicacion, id_administrador, conn=None):
        if conn is None:
            conn = sqlite3.connect('base_de_datos.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Estacion (nombre, ubicacion, id_administrador) VALUES (?, ?, ?)",
                (nombre, ubicacion, id_administrador)
            )
            conn.commit()

    @staticmethod
    def editar_estacion(id_estacion, nombre, ubicacion, conn=None):
        if conn is None:
            conn = sqlite3.connect('base_de_datos.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE Estacion SET nombre = ?, ubicacion = ? WHERE id = ?",
                (nombre, ubicacion, id_estacion)
            )
            conn.commit()

    @staticmethod
    def eliminar_estacion(id_estacion, conn=None):
        if conn is None:
            conn = sqlite3.connect('base_de_datos.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Estacion WHERE id = ?", (id_estacion,))
            conn.commit()
