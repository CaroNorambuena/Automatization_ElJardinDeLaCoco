"Creación de Base de Datos SQL desde Python"

# Importar el conector desde el motor
import mysql.connector as db 
                            
# Crear un objeto de conexión usando el conector                    
mydb = db.connect(
    host = "localhost",
    user = "root",
    passwd = "mysql123",
    port = 3306,
    database = ""
)

# Crear un cursor usando el objeto de conexión
my_cursor = mydb.cursor()

# Crear una sentencia SQL
sqlsentence = "CREATE DATABASE Inventario"

# Ejecutar la sentencia (se envía al motor)
my_cursor.execute(sqlsentence)