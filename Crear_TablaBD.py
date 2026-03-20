"Crear tablas en Base de Datos SQL"

# Importar el conector desde el motor
import mysql.connector as db 
                            
# Crear un objeto de conexión usando el conector                    
mydb = db.connect(
    host = "localhost",
    user = "root",
    passwd = "mysql123",
    port = 3306,
    database = "Inventario"  # Base de datos donde queremos crear la tabla
)

# Crear un cursor usando el objeto de conexión
my_cursor = mydb.cursor()

# Crear una sentencia SQL
sqlsentence = "CREATE TABLE Productos(id INTEGER AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(45), cantidad INTEGER(10), \
    precio INTEGER(10), código VARCHAR(45))"

# Nombre de la tabla: users (atributo1 TIPO DE DATO, atributo2 TIPO DE DATO, \
# atributo3 TIPO DE DATO, atributo4 TIPO DE DATO AUTO_INCREMENT PRIMARY KEY)
# AUTO_INCREMENT: se va agregando un numero automaticamente
# PRIMARY KEY: es una llave primaria

# Ejecutar la sentencia (se envía al motor)
my_cursor.execute(sqlsentence)

# Si el output es = 0 , funcionó!!
# Luego, hacer click en actualizar en MySQL Workbench