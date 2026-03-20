"Agregar información a tablas en Base de Datos SQL"

# Importar el conector desde el motor
import mysql.connector as db 
                            
# Crear un objeto de conexión usando el conector                    
mydb = db.connect(
    host = "localhost",
    user = "root",
    passwd = "mysql123",
    port = 3306,
    database = "Inventario"
)

# Crear un cursor usando el objeto de conexión
my_cursor = mydb.cursor()

# Crear una sentencia SQL
sqlsentence = "INSERT INTO Productos(nombre, cantidad, precio, código) VALUES (%s, %s, %s, %s)"  
fila = ("Sustrato cactus y suculentas", 10, 8990, "A100000000A")

# La clave primaria no es necesario indicarla, porque anteriormente se definió como AUTO_INCREMENT
# %s: son espacios preparados para recibir los valores
# Los valores se preparan como una tupla python = fila

# Ejecutar la sentencia (se envía al motor)
my_cursor.execute(sqlsentence, fila)

# Para hacer que los cambios sean definitivos
mydb.commit()