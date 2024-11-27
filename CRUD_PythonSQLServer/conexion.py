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
        """Cierra la conexión y el cursor."""
        self.cursor.close()
        self.conn.close()

    # Métodos para Persona
    @staticmethod
    def mostrarPersonas():
        conn = CConexion()
        conn.cursor.execute("SELECT persona_id, nombre, apellido, telefono, correo FROM Persona")
        personas = conn.cursor.fetchall()
        conn.cerrar_conexion()
        return personas

    @staticmethod
    def ingresarPersona(nombre, apellido, telefono, correo):
        conn = CConexion()
        conn.cursor.execute(
            "INSERT INTO Persona (nombre, apellido, telefono, correo) VALUES (?, ?, ?, ?)",
            (nombre, apellido, telefono, correo)
        )
        conn.conn.commit()
        conn.cerrar_conexion()

    @staticmethod
    def modificarPersona(id_persona, nombre, apellido, telefono, correo):
        conn = CConexion()
        conn.cursor.execute(
            "UPDATE Persona SET nombre = ?, apellido = ?, telefono = ?, correo = ? WHERE persona_id = ?",
            (nombre, apellido, telefono, correo, id_persona)
        )
        conn.conn.commit()
        conn.cerrar_conexion()

    @staticmethod
    def eliminarPersona(id_persona):
        conn = CConexion()
        conn.cursor.execute("DELETE FROM Persona WHERE persona_id = ?", (id_persona,))
        conn.conn.commit()
        conn.cerrar_conexion()

    @staticmethod
    def obtenerPersonaPorId(persona_id):
        conn = CConexion()
        conn.cursor.execute("SELECT persona_id, nombre, apellido FROM Persona WHERE persona_id = ?", (persona_id,))
        persona = conn.cursor.fetchone()
        conn.cerrar_conexion()
        return persona

    # Métodos para Mascota
    @staticmethod
    def mostrarMascotas():
        conn = CConexion()
        conn.cursor.execute("SELECT idmascota, nombre, tipo_mascota, raza, sexo, edad, persona_id FROM Mascota")
        mascotas = conn.cursor.fetchall()
        conn.cerrar_conexion()
        return mascotas

    @staticmethod
    def ingresarMascota(nombre, tipo, raza, sexo, edad, persona_id):
        conn = CConexion()
        conn.cursor.execute(
            "INSERT INTO Mascota (nombre, tipo_mascota, raza, sexo, edad, persona_id) VALUES (?, ?, ?, ?, ?, ?)",
            (nombre, tipo, raza, sexo, edad, persona_id)
        )
        conn.conn.commit()
        conn.cerrar_conexion()

    @staticmethod
    def modificarMascota(id_mascota, nombre, tipo, raza, sexo, edad, persona_id):
        conn = CConexion()
        conn.cursor.execute(
            "UPDATE Mascota SET nombre = ?, tipo_mascota = ?, raza = ?, sexo = ?, edad = ?, persona_id = ? WHERE idmascota = ?",
            (nombre, tipo, raza, sexo, edad, persona_id, id_mascota)
        )
        conn.conn.commit()
        conn.cerrar_conexion()

    @staticmethod
    def eliminarMascota(id_mascota):
        conn = CConexion()
        conn.cursor.execute("DELETE FROM Mascota WHERE idmascota = ?", (id_mascota,))
        conn.conn.commit()
        conn.cerrar_conexion()

    @staticmethod
    def obtenerMascotaPorId(idmascota):
        conn = CConexion()
        conn.cursor.execute("SELECT idmascota, nombre, tipo_mascota, raza, sexo, edad, persona_id FROM Mascota WHERE idmascota = ?", (idmascota,))
        mascota = conn.cursor.fetchone()
        conn.cerrar_conexion()
        return mascota

@staticmethod
def buscarInformacion(texto):
    """Busca coincidencias en las tablas de personas y mascotas."""
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
        cursor = conn.cursor  # Corregir aquí

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
        conn.cerrar_conexion()  # Asegúrate de cerrar la conexión correctamente
