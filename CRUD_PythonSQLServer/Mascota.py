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
        try:
            self.dueños = CConexion.mostrarPersonas()
            self.comboDueño['values'] = [f"{dueño[0]} - {dueño[1]} {dueño[2]}" for dueño in self.dueños]
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron cargar los dueños: {e}")


    def guardarRegistros(self):
        try:
            nombre = self.texBoxNombre.get().strip()
            tipo = self.comboTipo.get().strip()
            raza = self.texBoxRaza.get().strip()
            sexo = self.comboSexo.get().strip()
            edad = self.texBoxEdad.get().strip()
            dueño = self.comboDueño.get().strip()

            # Validaciones
            if not nombre or not tipo or not raza or not sexo or not edad or not dueño:
                messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
                return

            # Obtener el ID del dueño seleccionado
            dueño_id = dueño.split(" - ")[0]

            # Guardar la mascota
            CConexion.ingresarMascota(nombre, tipo, raza, sexo, edad, dueño_id)
            self.actualizarTreeView()
            messagebox.showinfo("Información", "Registro guardado exitosamente")

            # Limpiar campos
            self.limpiarCampos()

            # Recargar la lista de dueños
            self.cargarPersonas()  # Actualiza la lista de dueños

        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron guardar los datos: {e}")

    def actualizarTreeView(self):
        try:
            # Limpiar Treeview
            for item in self.tree.get_children():
                self.tree.delete(item)

            # Insertar nuevos datos
            for row in CConexion.mostrarMascotas():
                # Obtener el nombre del dueño
                dueño = CConexion.obtenerPersonaPorId(row[6])  # persona_id está en la posición 7
                dueño_nombre = f"{dueño[1]} {dueño[2]}" if dueño else "Desconocido"

                # Insertar en TreeView (omite la imagen si no quieres mostrarla)
                self.tree.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[5], dueño_nombre))
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron cargar los datos: {e}")

    def seleccionarRegistro(self, event):
        try:
            selected_item = self.tree.focus()
            if selected_item:
                values = self.tree.item(selected_item)['values']
                self.texBoxId.delete(0, END)
                self.texBoxId.insert(0, values[0])
                self.texBoxNombre.delete(0, END)
                self.texBoxNombre.insert(0, values[1])
                self.comboTipo.set(values[2])  # Corregido: establecer el valor del tipo de mascota
                self.texBoxRaza.delete(0, END)
                self.texBoxRaza.insert(0, values[3])
                self.comboSexo.set(values[4])  # Corregido: establecer el valor del sexo
                self.texBoxEdad.delete(0, END)
                self.texBoxEdad.insert(0, values[5])

                # Seleccionar el dueño en el combobox
                dueño_texto = ""
                for dueño in self.dueños:
                    if f"{dueño[1]} {dueño[2]}" == values[6]:
                        dueño_texto = f"{dueño[0]} - {dueño[1]} {dueño[2]}"
                        break
                self.comboDueño.set(dueño_texto)  # Corregido: establecer el valor del dueño
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron cargar los datos seleccionados: {e}")

    def modificarRegistros(self):
        try:
            id_mascota = self.texBoxId.get()
            nombre = self.texBoxNombre.get()
            tipo = self.comboTipo.get()
            raza = self.texBoxRaza.get()
            sexo = self.comboSexo.get()
            edad = self.texBoxEdad.get()
            dueño = self.comboDueño.get()

            if not id_mascota:
                messagebox.showwarning("Advertencia", "Debes seleccionar una mascota para modificar.")
                return

            dueño_id = dueño.split(" - ")[0]  # Obtener el ID del dueño seleccionado
            CConexion.modificarMascota(id_mascota, nombre, tipo, raza, sexo, edad, dueño_id)
            self.actualizarTreeView()
            messagebox.showinfo("Información", "Registro modificado exitosamente")
            self.limpiarCampos()

        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron modificar los datos: {e}")

    def eliminarRegistros(self):
        try:
            id_mascota = self.texBoxId.get()
            if not id_mascota:
                messagebox.showwarning("Advertencia", "Debes seleccionar una mascota para eliminar.")
                return

            respuesta = messagebox.askyesno("Confirmación", "¿Estás seguro de eliminar esta mascota?")
            if respuesta:
                CConexion.eliminarMascota(id_mascota)
                self.actualizarTreeView()
                messagebox.showinfo("Información", "Registro eliminado exitosamente")
                self.limpiarCampos()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron eliminar los datos: {e}")

    def limpiarCampos(self):
        self.texBoxId.delete(0, END)
        self.texBoxNombre.delete(0, END)
        self.comboTipo.set("")
        self.texBoxRaza.delete(0, END)
        self.comboSexo.set("")
        self.texBoxEdad.delete(0, END)
        self.comboDueño.set("")
