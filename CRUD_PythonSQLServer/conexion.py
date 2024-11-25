import pyodbc

class CConexion:
    def __init__(self):
        self.conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=ALI\\JESSICASQL;'
            'DATABASE=Crud;'
            'UID=Oficial;'
            'PWD=1234;'
        )
        self.cursor = self.conn.cursor()

    def cerrar_conexion(self):
        #Cierra la conexión y el cursor
        self.cursor.close()
        self.conn.close()

    # Métodos para Persona
    @staticmethod
    def mostrarPersonas():
        pass

    @staticmethod
    def ingresarPersona(nombre, apellido, telefono, correo):
        pass

    @staticmethod
    def modificarPersona(id_persona, nombre, apellido, telefono, correo):
        pass

    @staticmethod
    def eliminarPersona(id_persona):
        pass

    @staticmethod
    def obtenerPersonaPorId(persona_id):
        pass

    # Métodos para Mascota
    @staticmethod
    def mostrarMascotas():
        pass

    @staticmethod
    def ingresarMascota(nombre, tipo, raza, sexo, edad, persona_id):
        pass

    @staticmethod
    def modificarMascota(id_mascota, nombre, tipo, raza, sexo, edad, persona_id):
        pass

    @staticmethod
    def eliminarMascota(id_mascota):
        pass

    @staticmethod
    def obtenerMascotaPorId(idmascota):
        pass

# Métodos para Informacion
@staticmethod
def buscarInformacion(texto):
    #Busca datos en las tablas de personas y mascotas
    try:
        conn = CConexion()
        texto_busqueda = f"%{texto}%"
        query = """
        SELECT p.persona_id, p.nombre, p.apellido, m.idmascota, m.nombre AS mascota_nombre, m.tipo_mascota
        FROM Persona p
        LEFT JOIN Mascota m ON p.persona_id = m.persona_id
        WHERE p.nombre LIKE ? OR m.nombre LIKE ?
        """
        conn.cursor.execute(query, (texto_busqueda, texto_busqueda))
        resultados = conn.cursor.fetchall()
        return resultados
    except Exception as e:
        print("Error en la consulta:", e)
        return None
    finally:
        conn.cerrar_conexion()

@staticmethod
def obtener_datos_por_nombre(nombre):
    try:
        conn = CConexion()
        cursor = conn.cursor 

        # Consulta para obtener la persona
        query_persona = "SELECT persona_id, nombre, apellido, telefono, correo FROM Persona WHERE nombre LIKE ?"
        cursor.execute(query_persona, ('%' + nombre + '%',))
        persona = cursor.fetchone()

        if persona:
            # Consulta para obtener la mascota
            persona_id = persona[0]  # persona_id está en la primera posición
            query_mascota = "SELECT nombre, tipo_mascota, raza, sexo, edad FROM Mascota WHERE persona_id = ?"
            cursor.execute(query_mascota, (persona_id,))
            mascota = cursor.fetchone()

            # Construye y retorna como diccionario
            return {
                "persona": {
                    "nombre": persona[1],
                    "apellido": persona[2],
                    "telefono": persona[3],
                    "correo": persona[4],
                },
                "mascota": {
                    "nombre": mascota[0] if mascota else None,
                    "tipo": mascota[1] if mascota else None,
                    "raza": mascota[2] if mascota else None,
                    "sexo": mascota[3] if mascota else None,
                    "edad": mascota[4] if mascota else None,
                }
            }
        return None
    except Exception as e:
        print("Error en la consulta:", e)
        return None
    finally:
        conn.cerrar_conexion()  # cerrar la conexión
