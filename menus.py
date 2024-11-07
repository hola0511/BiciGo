import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from logica.gestor_usuarios import GestorUsuarios
from logica.gestor_cliente import GestorCliente
from logica.gestor_reserva import GestorReserva
from logica.gestor_estacion import GestorEstacion
from logica.notificacion import Notificacion

class MenuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Bicicletas")
        self.root.geometry("720x480")
        self.usuario_actual = None
        self.crear_menu_principal()

    def crear_menu_principal(self):
        self.limpiar_ventana()
        tk.Label(self.root, text="Menú Principal", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.root, text="Registrar Usuario", command=self.registrar_usuario, font=("Arial", 14), padx=10,
                  pady=5).pack(pady=10)
        tk.Button(self.root, text="Iniciar Sesión Cliente", command=self.iniciar_sesion_cliente, font=("Arial", 14),
                  padx=10, pady=5).pack(pady=10)
        tk.Button(self.root, text="Iniciar Sesión Administrador", command=self.iniciar_sesion_administrador,
                  font=("Arial", 14), padx=10, pady=5).pack(pady=10)
        tk.Button(self.root, text="Salir", command=self.root.quit, font=("Arial", 14), padx=10, pady=5,
                  bg="#FFCCCC").pack(pady=10)

    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def registrar_usuario(self):
        self.limpiar_ventana()
        tk.Label(self.root, text="Registrar Usuario", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="Nombre:").pack()
        nombre = tk.Entry(self.root, width=30)
        nombre.pack()
        tk.Label(self.root, text="Correo:").pack()
        correo = tk.Entry(self.root, width=30)
        correo.pack()
        tk.Label(self.root, text="Contraseña:").pack()
        contrasena = tk.Entry(self.root, show="*", width=30)
        contrasena.pack()
        rol = tk.IntVar()
        tk.Checkbutton(self.root, text="Es administrador", variable=rol).pack(pady=5)

        def registrar():
            GestorUsuarios.registrar_usuario(nombre.get(), correo.get(), contrasena.get(), rol.get())
            messagebox.showinfo("Registro", "Usuario registrado exitosamente")
            self.crear_menu_principal()
        tk.Button(self.root, text="Registrar", command=registrar, font=("Arial", 14), padx=10, pady=5).pack(pady=10)
        tk.Button(self.root, text="Volver", command=self.crear_menu_principal, font=("Arial", 14), padx=10, pady=5,
                  bg="#FFCCCC").pack(pady=10)

    def iniciar_sesion_cliente(self):
        self.iniciar_sesion(rol=False)

    def iniciar_sesion_administrador(self):
        self.iniciar_sesion(rol=True)

    def iniciar_sesion(self, rol):
        self.limpiar_ventana()
        tk.Label(self.root, text="Iniciar Sesión", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="Correo:").pack()
        correo = tk.Entry(self.root, width=30)
        correo.pack()
        tk.Label(self.root, text="Contraseña:").pack()
        contrasena = tk.Entry(self.root, show="*", width=30)
        contrasena.pack()

        def login():
            self.usuario_actual = GestorUsuarios.login_usuario(correo.get(), contrasena.get(), rol)
            if self.usuario_actual:
                messagebox.showinfo("Inicio de sesión", "Inicio de sesión exitoso")
                if rol:
                    self.mostrar_menu_administrador()
                else:
                    self.mostrar_menu_usuario()
            else:
                messagebox.showerror("Error", "Credenciales incorrectas")
        tk.Button(self.root, text="Iniciar sesión", command=login, font=("Arial", 14), padx=10, pady=5).pack(pady=10)
        tk.Button(self.root, text="Volver", command=self.crear_menu_principal, font=("Arial", 14), padx=10, pady=5,
                  bg="#FFCCCC").pack(pady=10)

    def mostrar_menu_usuario(self):
        self.limpiar_ventana()
        tk.Label(self.root, text="Menú Usuario", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.root, text="Reservar Bicicleta", command=self.reservar_bicicleta, font=("Arial", 14), padx=10,
                  pady=5).pack(pady=10)
        tk.Button(self.root, text="Consultar Historial de Reservas", command=self.consultar_historial,
                  font=("Arial", 14), padx=10, pady=5).pack(pady=10)
        tk.Button(self.root, text="Crear Queja", command=self.crear_queja, font=("Arial", 14), padx=10, pady=5).pack(
            pady=10)
        tk.Button(self.root, text="Cerrar Sesión", command=self.crear_menu_principal, font=("Arial", 14), padx=10,
                  pady=5, bg="#FFCCCC").pack(pady=10)

    def mostrar_menu_administrador(self):
        self.limpiar_ventana()
        tk.Label(self.root, text="Menú Administrador", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.root, text="Agregar Estación", command=self.agregar_estacion, font=("Arial", 14), padx=10,
                  pady=5).pack(pady=10)
        tk.Button(self.root, text="Editar Estación", command=self.editar_estacion, font=("Arial", 14), padx=10,
                  pady=5).pack(pady=10)
        tk.Button(self.root, text="Eliminar Estación", command=self.eliminar_estacion, font=("Arial", 14), padx=10,
                  pady=5).pack(pady=10)
        tk.Button(self.root, text="Cerrar Sesión", command=self.crear_menu_principal, font=("Arial", 14), padx=10,
                  pady=5, bg="#FFCCCC").pack(pady=10)

    def reservar_bicicleta(self):
        self.limpiar_ventana()
        tk.Label(self.root, text="Reservar Bicicleta", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="ID de la estación:").pack()
        estacion_id = tk.Entry(self.root, width=30)
        estacion_id.pack()
        tk.Label(self.root, text="ID de la distancia:").pack()
        distancia_id = tk.Entry(self.root, width=30)
        distancia_id.pack()

        def realizar_reserva():
            GestorReserva.crear_reserva(self.usuario_actual.id, estacion_id.get(), distancia_id.get())
            messagebox.showinfo("Reserva", "Reserva creada exitosamente")
            self.crear_menu_principal()
        tk.Button(self.root, text="Reservar", command=realizar_reserva, font=("Arial", 14), padx=10, pady=5).pack(
            pady=10)
        self.volver_boton()

    def consultar_historial(self):
        self.limpiar_ventana()
        tk.Label(self.root, text="Historial de Reservas", font=("Arial", 16)).pack(pady=10)

        # Crear una tabla usando Treeview
        columnas = ("fecha", "distancia", "tiempo", "hora")
        tabla = ttk.Treeview(self.root, columns=columnas, show="headings", height=10)
        tabla.heading("fecha", text="Fecha:")
        tabla.heading("distancia", text="Distancia:")
        tabla.heading("tiempo", text="Tiempo:")
        tabla.heading("hora", text="Hora:")
        tabla.column("fecha", anchor="center", width=150)
        tabla.column("distancia", anchor="center", width=100)
        tabla.column("tiempo", anchor="center", width=100)
        tabla.column("hora", anchor="center", width=100)
        historial = GestorCliente.consultar_historial(self.usuario_actual.id)
        if historial:
            for reserva in historial:
                fecha, distancia, tiempo, hora = reserva[1], f"{reserva[2]} KM", f"{reserva[3]} minutos", reserva[4]
                tabla.insert("", "end", values=(fecha, distancia, tiempo, hora))
        else:
            messagebox.showinfo("Historial", "No hay reservas en el historial.")
        tabla.pack(pady=10)
        self.volver_boton()

    def crear_queja(self):
        self.limpiar_ventana()
        tk.Label(self.root, text="Crear Queja", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="Motivo de la queja:").pack()
        razon = tk.Entry(self.root, width=30)
        razon.pack()
        tk.Label(self.root, text="ID de la estación:").pack()
        id_estacion = tk.Entry(self.root, width=30)
        id_estacion.pack()

        def registrar_queja():
            GestorCliente.crear_queja(self.usuario_actual.id, razon.get(), id_estacion.get())
            messagebox.showinfo("Queja", "Queja registrada exitosamente")
            self.crear_menu_principal()
        tk.Button(self.root, text="Registrar Queja", command=registrar_queja, font=("Arial", 14), padx=10, pady=5).pack(
            pady=10)
        self.volver_boton()

    def agregar_estacion(self):
        self.limpiar_ventana()
        tk.Label(self.root, text="Agregar Estación", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="Nombre de la estación:").pack()
        nombre = tk.Entry(self.root, width=30)
        nombre.pack()
        tk.Label(self.root, text="Ubicación de la estación:").pack()
        ubicacion = tk.Entry(self.root, width=30)
        ubicacion.pack()

        def agregar():
            GestorEstacion.agregar_estacion(nombre.get(), ubicacion.get(), self.usuario_actual.id)
            messagebox.showinfo("Estación", "Estación agregada exitosamente")
            self.crear_menu_principal()
        tk.Button(self.root, text="Agregar Estación", command=agregar, font=("Arial", 14), padx=10, pady=5).pack(
            pady=10)
        self.volver_boton()

    def editar_estacion(self):
        self.limpiar_ventana()
        tk.Label(self.root, text="Editar Estación", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="ID de la estación a editar:").pack()
        id_estacion = tk.Entry(self.root, width=30)
        id_estacion.pack()
        tk.Label(self.root, text="Nuevo nombre de la estación:").pack()
        nombre = tk.Entry(self.root, width=30)
        nombre.pack()
        tk.Label(self.root, text="Nueva ubicación de la estación:").pack()
        ubicacion = tk.Entry(self.root, width=30)
        ubicacion.pack()

        def editar():
            GestorEstacion.editar_estacion(id_estacion.get(), nombre.get(), ubicacion.get())
            messagebox.showinfo("Estación", "Estación editada exitosamente")
            self.crear_menu_principal()
        tk.Button(self.root, text="Editar Estación", command=editar, font=("Arial", 14), padx=10, pady=5).pack(pady=10)
        self.volver_boton()

    def eliminar_estacion(self):
        self.limpiar_ventana()
        tk.Label(self.root, text="Eliminar Estación", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="ID de la estación a eliminar:").pack()
        id_estacion = tk.Entry(self.root, width=30)
        id_estacion.pack()

        def eliminar():
            GestorEstacion.eliminar_estacion(id_estacion.get())
            messagebox.showinfo("Estación", "Estación eliminada exitosamente")
            self.crear_menu_principal()
        tk.Button(self.root, text="Eliminar Estación", command=eliminar, font=("Arial", 14), padx=10, pady=5).pack(
            pady=10)
        self.volver_boton()

    def volver_boton(self):
        tk.Button(self.root, text="Volver", command=self.crear_menu_principal, font=("Arial", 14), padx=10, pady=5,
                  bg="#FFCCCC").pack(pady=10)
