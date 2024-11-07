import unittest
import sqlite3
from logica.gestor_cliente import GestorCliente
from logica.gestor_estacion import GestorEstacion
from logica.gestor_reserva import GestorReserva


class TestBiciGoApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.conn = sqlite3.connect(':memory:')
        cls.cursor = cls.conn.cursor()

        # Crear las tablas en la base de datos de prueba
        cls.cursor.execute('''
            CREATE TABLE Queja (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_cliente INTEGER,
                razon TEXT,
                estado BOOLEAN,
                id_estacion INTEGER
            )
        ''')
        cls.cursor.execute('''
            CREATE TABLE Estacion (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                ubicacion TEXT,
                id_administrador INTEGER
            )
        ''')
        cls.cursor.execute('''
            CREATE TABLE Reserva (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha TEXT,
                hora TEXT,
                id_cliente INTEGER,
                id_estacion INTEGER,
                id_distancia INTEGER
            )
        ''')
        cls.conn.commit()

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()

    def setUp(self):
        # Limpiar las tablas antes de cada prueba
        self.cursor.execute("DELETE FROM Queja")
        self.cursor.execute("DELETE FROM Estacion")
        self.cursor.execute("DELETE FROM Reserva")
        self.conn.commit()

    def test_crear_queja(self):
        GestorCliente.crear_queja(1, "Bicicleta defectuosa", 1, self.conn)
        self.cursor.execute("SELECT * FROM Queja WHERE id_cliente = 1")
        queja = self.cursor.fetchone()
        self.assertIsNotNone(queja)
        self.assertEqual(queja[2], "Bicicleta defectuosa")

    def test_consultar_quejas_por_estacion(self):
        GestorCliente.crear_queja(1, "Bicicleta dañada", 2, self.conn)
        quejas = GestorCliente.consultar_quejas_por_estacion(2, self.conn)
        self.assertEqual(len(quejas), 1)
        self.assertEqual(quejas[0][2], "Bicicleta dañada")

    def test_agregar_estacion(self):
        GestorEstacion.agregar_estacion("Estación Central", "Centro", 1, self.conn)
        self.cursor.execute("SELECT * FROM Estacion WHERE nombre = 'Estación Central'")
        estacion = self.cursor.fetchone()
        self.assertIsNotNone(estacion)
        self.assertEqual(estacion[1], "Estación Central")

    def test_editar_estacion(self):
        GestorEstacion.agregar_estacion("Estación Norte", "Norte", 1, self.conn)
        self.cursor.execute("SELECT id FROM Estacion WHERE nombre = 'Estación Norte'")
        estacion_id = self.cursor.fetchone()[0]

        GestorEstacion.editar_estacion(estacion_id, "Estación Norte Editada", "Norte Editado", self.conn)
        self.cursor.execute("SELECT * FROM Estacion WHERE id = ?", (estacion_id,))
        estacion = self.cursor.fetchone()
        self.assertEqual(estacion[1], "Estación Norte Editada")
        self.assertEqual(estacion[2], "Norte Editado")

    def test_eliminar_estacion(self):
        GestorEstacion.agregar_estacion("Estación Sur", "Sur", 1, self.conn)
        self.cursor.execute("SELECT id FROM Estacion WHERE nombre = 'Estación Sur'")
        estacion_id = self.cursor.fetchone()[0]

        GestorEstacion.eliminar_estacion(estacion_id, self.conn)
        self.cursor.execute("SELECT * FROM Estacion WHERE id = ?", (estacion_id,))
        estacion = self.cursor.fetchone()
        self.assertIsNone(estacion)

    def test_crear_reserva(self):
        GestorReserva.crear_reserva(1, 1, 1, self.conn)
        self.cursor.execute("SELECT * FROM Reserva WHERE id_cliente = 1")
        reserva = self.cursor.fetchone()
        self.assertIsNotNone(reserva)
        self.assertEqual(reserva[3], 1)

    def test_consultar_historial(self):
        GestorReserva.crear_reserva(1, 1, 1, self.conn)
        historial = GestorCliente.consultar_historial(1, self.conn)
        self.assertEqual(len(historial), 1)
        self.assertEqual(historial[0][3], 1)
