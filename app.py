from logica import GestorUsuarios, GestorCliente, GestorReserva, GestorEstacion, Notificacion


class Menu:
    def __init__(self):
        self.usuario_actual = None

    def mostrar_menu_principal(self):
        while True:
            print("\n---- Menú Principal ----")
            print("1. Registrar Usuario")
            print("2. Iniciar Sesión Cliente")
            print("3. Iniciar Sesión Administrador")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registrar_usuario()
            elif opcion == "2":
                self.iniciar_sesion_cliente()
            elif opcion == "3":
                self.iniciar_sesion_administrador()
            elif opcion == "4":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida, intente nuevamente.")

    def registrar_usuario(self):
        nombre = input("Ingrese su nombre: ")
        correo = input("Ingrese su correo: ")
        contrasena = input("Ingrese su contraseña: ")
        rol = input("Es administrador? (s/n): ").lower() == 's'
        GestorUsuarios.registrar_usuario(nombre, correo, contrasena, rol)

    def iniciar_sesion_cliente(self):
        correo = input("Ingrese su correo: ")
        contrasena = input("Ingrese su contraseña: ")
        self.usuario_actual = GestorUsuarios.login_usuario(correo, contrasena, rol=False)
        if self.usuario_actual:
            self.mostrar_menu_usuario()

    def iniciar_sesion_administrador(self):
        correo = input("Ingrese su correo: ")
        contrasena = input("Ingrese su contraseña: ")
        self.usuario_actual = GestorUsuarios.login_usuario(correo, contrasena, rol=True)
        if self.usuario_actual:
            self.mostrar_menu_administrador()

    def mostrar_menu_usuario(self):
        while True:
            print("\n---- Menú Usuario ----")
            print("1. Reservar Bicicleta")
            print("2. Consultar Historial de Reservas")
            print("3. Crear Queja")
            print("4. Cerrar Sesión")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.reservar_bicicleta()
            elif opcion == "2":
                self.consultar_historial()
            elif opcion == "3":
                self.crear_queja()
            elif opcion == "4":
                print("Cerrando sesión de usuario...")
                self.usuario_actual = None
                break
            else:
                print("Opción inválida, intente nuevamente.")

    def mostrar_menu_administrador(self):
        while True:
            print("\n---- Menú Administrador ----")
            print("1. Agregar Estación")
            print("2. Editar Estación")
            print("3. Eliminar Estación")
            print("4. Cerrar Sesión")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_estacion()
            elif opcion == "2":
                self.editar_estacion()
            elif opcion == "3":
                self.eliminar_estacion()
            elif opcion == "4":
                print("Cerrando sesión de administrador...")
                self.usuario_actual = None
                break
            else:
                print("Opción inválida, intente nuevamente.")

    def reservar_bicicleta(self):
        id_estacion = int(input("Ingrese el ID de la estación: "))
        id_distancia = int(input("Ingrese el ID de la distancia: "))
        GestorReserva.crear_reserva(self.usuario_actual.id, id_estacion, id_distancia)

    def consultar_historial(self):
        GestorCliente.consultar_historial(self.usuario_actual.id)

    def crear_queja(self):
        razon = input("Ingrese el motivo de su queja: ")
        GestorCliente.crear_queja(self.usuario_actual.id, razon)

    def agregar_estacion(self):
        nombre = input("Ingrese el nombre de la estación: ")
        ubicacion = input("Ingrese la ubicación de la estación: ")
        GestorEstacion.agregar_estacion(nombre, ubicacion, self.usuario_actual.id)

    def editar_estacion(self):
        id_estacion = int(input("Ingrese el ID de la estación a editar: "))
        nombre = input("Ingrese el nuevo nombre de la estación: ")
        ubicacion = input("Ingrese la nueva ubicación de la estación: ")
        GestorEstacion.editar_estacion(id_estacion, nombre, ubicacion)

    def eliminar_estacion(self):
        id_estacion = int(input("Ingrese el ID de la estación a eliminar: "))
        GestorEstacion.eliminar_estacion(id_estacion)


# Ejecutar menú principal
if __name__ == "__main__":
    menu = Menu()
    menu.mostrar_menu_principal()
