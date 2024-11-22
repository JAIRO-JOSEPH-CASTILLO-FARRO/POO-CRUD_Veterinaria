import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from conexion import * 

class FormularioMascota:
    def __init__(self, parent):
        self.frame = tk.Frame(parent)
        self.interf_mascota()

    def interf_mascota(self):
        # Frame para el formulario
        group_box = LabelFrame(self.frame, text="FORMULARIO MASCOTA", font=("Cooper Black", 12), padx=10, pady=10)
        group_box.pack(fill="both", expand="yes", padx=10, pady=10)

        # Campos del formulario
        Label(group_box, text="ID:", width=15, font=("Cambria", 11)).grid(row=0, column=0, pady=5, sticky=W)
        self.texBoxId = Entry(group_box)
        self.texBoxId.grid(row=0, column=1, pady=5)

        Label(group_box, text="Nombre:", width=15, font=("Cambria", 11)).grid(row=1, column=0, pady=5, sticky=W)
        self.texBoxNombre = Entry(group_box)
        self.texBoxNombre.grid(row=1, column=1, pady=5)

        Label(group_box, text="Tipo de Mascota:", width=15, font=("Cambria", 11)).grid(row=2, column=0, pady=5, sticky=W)
        self.comboTipo = ttk.Combobox(group_box, values=["Perro", "Gato", "Hamster", "Pez", "Tortuga"], state="readonly")
        self.comboTipo.grid(row=2, column=1, pady=5)

        Label(group_box, text="Raza:", width=15, font=("Cambria", 11)).grid(row=3, column=0, pady=5, sticky=W)
        self.texBoxRaza = Entry(group_box)
        self.texBoxRaza.grid(row=3, column=1, pady=5)

        Label(group_box, text="Sexo:", width=15, font=("Cambria", 11)).grid(row=4, column=0, pady=5, sticky=W)
        self.comboSexo = ttk.Combobox(group_box, values=["Macho", "Hembra"], state="readonly")
        self.comboSexo.grid(row=4, column=1, pady=5)

        Label(group_box, text="Edad:", width=15, font=("Cambria", 11)).grid(row=5, column=0, pady=5, sticky=W)
        self.texBoxEdad = Entry(group_box)
        self.texBoxEdad.grid(row=5, column=1, pady=5)

        Label(group_box, text="Dueño:", width=15, font=("Cambria", 11)).grid(row=6, column=0, pady=5, sticky=W)
        self.comboDueño = ttk.Combobox(group_box, state="readonly")
        self.comboDueño.grid(row=6, column=1, pady=5)
        self.cargarPersonas()

        # Botones de acción
        Button(group_box, text="Guardar", width=10, font=("Britannic Bold", 11), fg="white", bg="green",
               command=self.guardarRegistros).grid(row=9, column=0, pady=10)
        Button(group_box, text="Modificar", width=10, font=("Britannic Bold", 11), fg="white", bg="orange",
               command=self.modificarRegistros).grid(row=9, column=1, pady=10)
        Button(group_box, text="Eliminar", width=10, font=("Britannic Bold", 11), fg="white", bg="red",
               command=self.eliminarRegistros).grid(row=9, column=2, pady=10)

        # Frame para la tabla de datos
        group_box_tabla = LabelFrame(self.frame, text="DATOS DE MASCOTAS", font=("Cooper Black", 12), padx=10, pady=10)
        group_box_tabla.pack(fill="both", expand="yes", padx=10, pady=10)

        # Configuración del Treeview
        self.tree = ttk.Treeview(group_box_tabla,
                                 columns=("ID", "Nombre", "Tipo", "Raza", "Sexo", "Edad", "Dueño"),
                                 show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Tipo", text="Tipo")
        self.tree.heading("Raza", text="Raza")
        self.tree.heading("Sexo", text="Sexo")
        self.tree.heading("Edad", text="Edad")
        self.tree.heading("Dueño", text="Dueño")

        self.tree.column("ID", anchor=CENTER, width=30)
        self.tree.column("Nombre", anchor=CENTER, width=100)
        self.tree.column("Tipo", anchor=CENTER, width=100)
        self.tree.column("Raza", anchor=CENTER, width=100)
        self.tree.column("Sexo", anchor=CENTER, width=80)
        self.tree.column("Edad", anchor=CENTER, width=50)
        self.tree.column("Dueño", anchor=CENTER, width=150)

        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.seleccionarRegistro)

        self.actualizarTreeView()

    def cargarPersonas(self):
        pass

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