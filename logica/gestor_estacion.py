import sqlite3

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
