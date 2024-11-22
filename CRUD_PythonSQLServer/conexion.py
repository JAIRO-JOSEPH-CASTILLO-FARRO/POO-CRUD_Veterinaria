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