import pyodbc

class Cconexion:

    @staticmethod
    def ConexionBaseDeDatos():
        try:
            conexion = pyodbc.connect(
                "DRIVER={ODBC Driver 17 for SQL Server};"
                "SERVER=ALI\\JESSICASQL;"
                "DATABASE=Crud;"
                "UID=Oficial;"
                "PWD=1234;"
            )
            print("Conectado a Microsoft SQL Server")

            return conexion

        except Exception as e:
            print(f"ERROR: No se pudo conectar a Microsoft SQL Server. {e}")
            return conexion

    ConexionBaseDeDatos()
