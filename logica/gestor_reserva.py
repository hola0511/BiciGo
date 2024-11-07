import sqlite3
from datetime import datetime

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
