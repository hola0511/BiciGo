import sqlite3

class GestorCliente:
    @staticmethod
    def crear_queja(cliente_id, razon, id_estacion):
        with sqlite3.connect('base_de_datos.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Queja (id_cliente, razon, estado, id_estacion) VALUES (?, ?, ?, ?)",
                           (cliente_id, razon, False, id_estacion))
            conn.commit()
            print("Queja registrada exitosamente.")

    @staticmethod
    def consultar_historial(cliente_id):
        with sqlite3.connect('base_de_datos.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Reserva WHERE id_cliente = ?", (cliente_id,))
            reservas = cursor.fetchall()
            return reservas

    @staticmethod
    def consultar_quejas_por_estacion(id_estacion):
        with sqlite3.connect('base_de_datos.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Queja WHERE id_estacion = ?", (id_estacion,))
            quejas = cursor.fetchall()
            return quejas
