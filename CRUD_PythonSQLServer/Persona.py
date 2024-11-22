import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from conexion import * #Importacion de la base de datos


class FormularioPersona:
    def __init__(self, parent):
        self.frame = tk.Frame(parent)
        self.interf_persona()

    def interf_persona(self):
        # Frame para el formulario
        group_box = LabelFrame(self.frame, text="FORMULARIO PERSONA", font=("Cooper Black", 12), padx=10, pady=10)
        group_box.pack(fill="both", expand="yes", padx=10, pady=10)

        # Campos del formulario
        Label(group_box, text="ID:", width=15, font=("Cambria", 11)).grid(row=0, column=0, pady=5, sticky=W)
        self.texBoxId = Entry(group_box)
        self.texBoxId.grid(row=0, column=1, pady=5)

        Label(group_box, text="Nombre:", width=15, font=("Cambria", 11)).grid(row=1, column=0, pady=5, sticky=W)
        self.texBoxNombre = Entry(group_box)
        self.texBoxNombre.grid(row=1, column=1, pady=5)

        Label(group_box, text="Apellido:", width=15, font=("Cambria", 11)).grid(row=2, column=0, pady=5, sticky=W)
        self.texBoxApellido = Entry(group_box)
        self.texBoxApellido.grid(row=2, column=1, pady=5)

        Label(group_box, text="Teléfono:", width=15, font=("Cambria", 11)).grid(row=3, column=0, pady=5, sticky=W)
        self.texBoxTelefono = Entry(group_box)
        self.texBoxTelefono.grid(row=3, column=1, pady=5)

        Label(group_box, text="Correo:", width=15, font=("Cambria", 11)).grid(row=4, column=0, pady=5, sticky=W)
        self.texBoxCorreo = Entry(group_box)
        self.texBoxCorreo.grid(row=4, column=1, pady=5)

        # Botones de acción
        Button(group_box, text="Guardar", width=10, font=("Britannic Bold", 11), fg="white", bg="green", command=self.guardarRegistros).grid(row=5, column=0, pady=10)
        Button(group_box, text="Modificar", width=10, font=("Britannic Bold", 11), fg="white", bg="orange", command=self.modificarRegistros).grid(row=5, column=1, pady=10)
        Button(group_box, text="Eliminar", width=10, font=("Britannic Bold", 11), fg="white", bg="red", command=self.eliminarRegistros).grid(row=5, column=2, pady=10)

        # Frame para la tabla de datos
        group_box_tabla = LabelFrame(self.frame, text="DATOS DE PERSONAS", font=("Cooper Black", 12), padx=10, pady=10 )
        group_box_tabla.pack(fill="both", expand="yes", padx=10, pady=10)

        # Configuración del Treeview
        self.tree = ttk.Treeview(group_box_tabla, columns=("ID", "Nombre", "Apellido", "Teléfono", "Correo"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Apellido", text="Apellido")
        self.tree.heading("Teléfono", text="Teléfono")
        self.tree.heading("Correo", text="Correo")

        self.tree.column("ID", anchor=CENTER, width=30)
        self.tree.column("Nombre", anchor=CENTER, width=100)
        self.tree.column("Apellido", anchor=CENTER, width=100)
        self.tree.column("Teléfono", anchor=CENTER, width=100)
        self.tree.column("Correo", anchor=CENTER, width=150)

        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.seleccionarRegistro)

        self.actualizarTreeView()

    def guardarRegistros(self):
        pass

    def actualizarTreeView(self):
        pass

    def seleccionarRegistro(self, event):
        pass

    def modificarRegistros(self):
        pass

    def eliminarRegistros(self):
        pass

    def limpiarCampos(self):
        pass
