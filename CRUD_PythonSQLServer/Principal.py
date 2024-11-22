import tkinter as tk
from PIL import Image, ImageTk  # Asegúrate de tener instalada la biblioteca Pillow

# Importación de las interfaces
from Persona import FormularioPersona
from Mascota import FormularioMascota
from Informacion import FormularioInformacion


class App:
    def __init__(self, root):
        # Configuración inicial de la ventana principal
        self.root = root
        self.root.title("Sistema Veterinario")  # Título de la ventana
        self.root.geometry("800x700")  # Tamaño de la ventana
        self.root.configure(bg="white")

        self.boton_seleccionado = None  # Botón seleccionado actualmente

        titulo_label = tk.Label(root,text="Bienvenido al Sistema Veterinario",bg="white", fg="#17BECF", font=("Cooper Black", 18), pady=10)
        titulo_label.pack(side=tk.TOP, fill=tk.X)

        # Crear el menú principal con botones de navegación
        menu_frame = tk.Frame(root, bg="white")
        menu_frame.pack(side=tk.TOP, fill=tk.X)

        # Botón para mostrar la interfaz de personas
        imagen_tk_personas = self.cargar_imagen("icono/btnPersona.png", (50, 50))
        self.btn_personas = tk.Button(menu_frame, text="PERSONAS", command=self.show_personas, bg="#17BECF", fg="white", font=("Cooper Black", 12))
        if imagen_tk_personas:
            self.btn_personas.config(image=imagen_tk_personas, compound=tk.RIGHT, padx=20)
            self.btn_personas.image = imagen_tk_personas
        self.btn_personas.pack(side=tk.LEFT, padx=5, pady=5)

        # Botón para mostrar la interfaz de mascotas
        imagen_tk_mascotas = self.cargar_imagen("icono/btnMascota.png", (50, 50))
        self.btn_mascotas = tk.Button(menu_frame, text="MASCOTAS", command=self.show_mascotas, bg="#17BECF", fg="white", font=("Cooper Black", 12))
        if imagen_tk_mascotas:
            self.btn_mascotas.config(image=imagen_tk_mascotas, compound=tk.RIGHT, padx=20)
            self.btn_mascotas.image = imagen_tk_mascotas
        self.btn_mascotas.pack(side=tk.LEFT, padx=5, pady=5)

        # Botón para mostrar la interfaz de información
        imagen_tk_informacion = self.cargar_imagen("icono/btnInformacion.png", (50, 50))
        self.btn_informacion = tk.Button(menu_frame, text="INFORMACIÓN", command=self.show_informacion, bg="#17BECF", fg="white", font=("Cooper Black", 12)
        )
        if imagen_tk_informacion:
            self.btn_informacion.config(image=imagen_tk_informacion, compound=tk.RIGHT, padx=20)
            self.btn_informacion.image = imagen_tk_informacion
        self.btn_informacion.pack(side=tk.LEFT, padx=5, pady=5)

        # Contenedor para las interfaces
        self.container = tk.Frame(root, bg="white")
        self.container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Inicializar las interfaces
        self.form_personas = FormularioPersona(self.container)  # Interfaz de personas
        self.form_mascotas = FormularioMascota(self.container)  # Interfaz de mascotas
        self.form_informacion = FormularioInformacion(self.container)  # Interfaz de información

        # Mostrar la interfaz inicial de personas
        self.show_personas()

    def cargar_imagen(self, ruta, size):
        """Carga y redimensiona una imagen."""
        try:
            imagen_pil = Image.open(ruta)
            imagen_resize = imagen_pil.resize(size)
            return ImageTk.PhotoImage(imagen_resize)
        except FileNotFoundError:
            print(f"Advertencia: La imagen '{ruta}' no existe.")
            return None
        except Exception as e:
            print(f"Error al cargar la imagen '{ruta}': {e}")
            return None

    def actualizar_color_boton(self, boton_actual):
        """Actualiza el color del botón seleccionado."""
        if self.boton_seleccionado:  # Restaurar el color del botón previamente seleccionado
            self.boton_seleccionado.config(bg="#17BECF", fg="white")
        boton_actual.config(bg="orange", fg="black")  # Cambiar el color del botón actual a naranja
        self.boton_seleccionado = boton_actual

    def show_personas(self):
        self.actualizar_color_boton(self.btn_personas)
        self.ocultar_todo()
        self.form_personas.frame.pack(fill=tk.BOTH, expand=True)

    def show_mascotas(self):
        self.actualizar_color_boton(self.btn_mascotas)
        self.ocultar_todo()
        self.form_mascotas.frame.pack(fill=tk.BOTH, expand=True)

    def show_informacion(self):
        self.actualizar_color_boton(self.btn_informacion)
        self.ocultar_todo()
        self.form_informacion.frame.pack(fill=tk.BOTH, expand=True)

    def ocultar_todo(self):
        self.form_personas.frame.pack_forget()
        self.form_mascotas.frame.pack_forget()
        self.form_informacion.frame.pack_forget()


# Iniciar la aplicación si este es el archivo principal
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()