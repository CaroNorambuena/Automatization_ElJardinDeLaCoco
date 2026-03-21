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
filas = [
    ("Sustrato para macetas", 10, 8990, "A100000001A"),
    ("Monstera", 10, 15000, "A100000002A"),
    ("Potos", 10, 8990, "A100000003A"),
    ("Lirio de la Paz", 10, 5500, "A100000004A"),
    ("Filodendro", 10, 18500, "A100000005A"),
    ("Violeta", 10, 7990, "A100000006A"),
    ("Rosas", 10, 20000, "A100000007A"),
    ("Manzanilla", 10, 3500, "A100000008A")
    ]


# La clave primaria no es necesario indicarla, porque anteriormente se definió como AUTO_INCREMENT
# %s: son espacios preparados para recibir los valores
# Los valores se preparan como una tupla python = fila

# Ejecutar la sentencia (se envía al motor)
# Nota: Se usa executemany() para múltiples filas
my_cursor.executemany(sqlsentence, filas)

# Para hacer que los cambios sean definitivos
mydb.commit()