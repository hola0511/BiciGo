import sqlite3

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
