import tkinter as tk
from tkinter import LabelFrame, Label, Entry, Button, W
import os  # Para manejar el sistema de archivos
from conexion import *

class FormularioInformacion:
    def __init__(self, parent):
        self.frame = tk.Frame(parent)
        self.frame.pack(fill="both", expand=True)  # Asegura que se muestre correctamente
        self.interf_info()

    def interf_info(self):
        # Frame de Búsqueda
        search_box = LabelFrame(self.frame, padx=10, pady=10)
        search_box.pack(fill="both", expand="yes", padx=5, pady=5)

        Label(search_box, text="Buscar por nombre:", font=("Cambria", 11)).grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.entry_busqueda = Entry(search_box, width=40)
        self.entry_busqueda.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        Button(search_box, text="🔎", width=4, font=("Britannic Bold", 12), bg="white", fg="black",
               command=self.buscar_registros).grid(row=0, column=2, padx=10)
        Button(search_box, text="Limpiar", width=10, font=("Britannic Bold", 11), bg="gray", fg="white",
               command=self.limpiar_busqueda).grid(row=0, column=3, padx=10)

        # Frame para el formulario Persona
        group_box_persona = LabelFrame(self.frame, text="FORMULARIO PERSONA", font=("Cooper Black", 12), padx=10, pady=10)
        group_box_persona.pack(fill="both", expand="yes", padx=10, pady=10)

        # Campos del formulario Persona

        Label(group_box_persona, text="Nombre:", width=15, font=("Cambria", 11)).grid(row=0, column=0, pady=5, sticky=W)
        self.texBoxNombre = Entry(group_box_persona)
        self.texBoxNombre.grid(row=0, column=1, pady=5)

        Label(group_box_persona, text="Apellido:", width=15, font=("Cambria", 11)).grid(row=1, column=0, pady=5, sticky=W)
        self.texBoxApellido = Entry(group_box_persona)
        self.texBoxApellido.grid(row=1, column=1, pady=5)

        Label(group_box_persona, text="Teléfono:", width=15, font=("Cambria", 11)).grid(row=2, column=0, pady=5, sticky=W)
        self.texBoxTelefono = Entry(group_box_persona)
        self.texBoxTelefono.grid(row=2, column=1, pady=5)

        Label(group_box_persona, text="Correo:", width=15, font=("Cambria", 11)).grid(row=3, column=0, pady=5, sticky=W)
        self.texBoxCorreo = Entry(group_box_persona)
        self.texBoxCorreo.grid(row=3, column=1, pady=5)

        # Frame para el formulario Mascota
        group_box_mascota = LabelFrame(self.frame, text="FORMULARIO MASCOTA", font=("Cooper Black", 12), padx=10, pady=10)
        group_box_mascota.pack(fill="both", expand="yes", padx=10, pady=10)

        # Campos del formulario Mascota

        Label(group_box_mascota, text="Nombre:", width=15, font=("Cambria", 11)).grid(row=0, column=0, pady=5, sticky=W)
        self.texBoxMascotaNombre = Entry(group_box_mascota)
        self.texBoxMascotaNombre.grid(row=0, column=1, pady=5)

        Label(group_box_mascota, text="Tipo de mascota:", width=15, font=("Cambria", 11)).grid(row=1, column=0, pady=5, sticky=W)
        self.texBoxTipo = Entry(group_box_mascota)
        self.texBoxTipo.grid(row=1, column=1, pady=5)

        Label(group_box_mascota, text="Raza:", width=15, font=("Cambria", 11)).grid(row=2, column=0, pady=5, sticky=W)
        self.texBoxRaza = Entry(group_box_mascota)
        self.texBoxRaza.grid(row=2, column=1, pady=5)

        Label(group_box_mascota, text="Sexo:", width=15, font=("Cambria", 11)).grid(row=3, column=0, pady=5, sticky=W)
        self.texBoxSexo = Entry(group_box_mascota)
        self.texBoxSexo.grid(row=3, column=1, pady=5)

        Label(group_box_mascota, text="Edad:", width=15, font=("Cambria", 11)).grid(row=4, column=0, pady=5, sticky=W)
        self.texBoxEdad = Entry(group_box_mascota)
        self.texBoxEdad.grid(row=4, column=1, pady=5)

    def buscar_registros(self):
        nombre = self.entry_busqueda.get()
        datos = obtener_datos_por_nombre(nombre)

        if datos:
            persona, mascota = datos["persona"], datos["mascota"]
            
            # Rellenar datos de persona
            self.texBoxNombre.delete(0, tk.END)
            self.texBoxNombre.insert(0, persona["nombre"])
            self.texBoxApellido.delete(0, tk.END)
            self.texBoxApellido.insert(0, persona["apellido"])
            self.texBoxTelefono.delete(0, tk.END)
            self.texBoxTelefono.insert(0, persona["telefono"])
            self.texBoxCorreo.delete(0, tk.END)
            self.texBoxCorreo.insert(0, persona["correo"])

            # Rellenar datos de mascota
            self.texBoxMascotaNombre.delete(0, tk.END)
            self.texBoxMascotaNombre.insert(0, mascota["nombre"] if mascota else "Sin mascota")
            self.texBoxTipo.delete(0, tk.END)
            self.texBoxTipo.insert(0, mascota["tipo"] if mascota else "N/A")
            self.texBoxRaza.delete(0, tk.END)
            self.texBoxRaza.insert(0, mascota["raza"] if mascota else "N/A")
            self.texBoxSexo.delete(0, tk.END)
            self.texBoxSexo.insert(0, mascota["sexo"] if mascota else "N/A")
            self.texBoxEdad.delete(0, tk.END)
            self.texBoxEdad.insert(0, mascota["edad"] if mascota else "N/A")
        else:
            print("No se encontraron resultados.")

    def limpiar_busqueda(self):
        self.entry_busqueda.delete(0, tk.END)
        self.texBoxNombre.delete(0, tk.END)
        self.texBoxApellido.delete(0, tk.END)
        self.texBoxTelefono.delete(0, tk.END)
        self.texBoxCorreo.delete(0, tk.END)
        self.texBoxMascotaNombre.delete(0, tk.END)
        self.texBoxTipo.delete(0, tk.END)
        self.texBoxRaza.delete(0, tk.END)
        self.texBoxSexo.delete(0, tk.END)
        self.texBoxEdad.delete(0, tk.END)
