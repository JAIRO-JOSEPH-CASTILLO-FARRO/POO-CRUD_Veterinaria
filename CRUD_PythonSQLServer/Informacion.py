import tkinter as tk
from tkinter import LabelFrame, Label, Entry, Button, W
from conexion import *

class FormularioInformacion:
    def __init__(self, parent):
        self.frame = tk.Frame(parent)
        self.interf_info()

    def interf_info(self):
        # Frame de Búsqueda
        search_box = LabelFrame(self.frame, padx=10, pady=10)
        search_box.pack(fill="both", expand="yes", padx=5, pady=5)

        Label(search_box, text="Buscar por nombre:", font=("Cambria", 11)).grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.entry_busqueda = Entry(search_box, width=40)
        self.entry_busqueda.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        Button(search_box, text="🔎", width=4, font=("Britannic Bold", 12), bg="white", fg="black", command=self.buscar_registros).grid(row=0, column=2, padx=10)
        Button(search_box, text="Limpiar", width=10, font=("Britannic Bold", 11), bg="gray", fg="white", command=self.limpiar_busqueda).grid(row=0, column=3, padx=10)

        # Frame para mostrar los datos de personas
        self.group_box_personas = LabelFrame(self.frame, text="DATOS DE PERSONAS", font=("Cooper Black", 11), padx=10, pady=10)
        self.group_box_personas.pack(fill="both", expand="yes", padx=10, pady=10)

        # Frame para mostrar los datos de mascotas
        self.group_box_mascotas = LabelFrame(self.frame, text="DATOS DE MASCOTAS", font=("Cooper Black", 11), padx=10, pady=10)
        self.group_box_mascotas.pack(fill="both", expand="yes", padx=10, pady=10)

    def buscar_registros(self):
        pass

    def limpiar_busqueda(self):
        pass

    def actualizar_vistas(self):
        pass
