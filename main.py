
import cv2
from pyzbar.pyzbar import decode


def codigo():
        # INPUT USUARIO
        nombre_archivo = entrada.get() #con get se obtiene lo que se escribe en "entrada" y se guarda como nombre_archivo

        # Cargar imagen
        imagen = cv2.imread(nombre_archivo) # Foto tomada con el celular

        # Verificar que la imagen se cargó correctamente
        if imagen is None:
            print("Error: No se pudo cargar la imagen.")
            # exit() # Detener la ejecución

        # Convertir a escala de grises (mejora detección)
        gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

        # Detectar códigos de barras
        codigos = decode(gris) # Devuelve una lista de objetos. Cada uno tiene atributos
        print(codigos)

        if not codigos:
            print("No se detectó ningún código de barras.")
        else:
            # Iterar la lista codigos. Cada elemento de la lista se llama codigo
            for codigo in codigos: 
                # Extraer datos
                datos = codigo.data.decode("utf-8") # Extrae el atributo data y luego los muestra en UTF-8
                tipo = codigo.type # Extrae el atributo type

                print(f"Código detectado: {datos}")
                print(f"Tipo: {tipo}")

                # # Dibujar rectángulo alrededor del código
                # x, y, w, h = codigo.rect
                # cv2.rectangle(imagen, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # # Mostrar texto encima
                # cv2.putText(imagen, datos, (x, y - 10),
                #             cv2.FONT_HERSHEY_SIMPLEX,
                #             0.5, (0, 255, 0), 2)


        import mysql.connector as db

        # Conexión
        mydb = db.connect(
            host="localhost",
            user="root",
            port = 3306,
            passwd="mysql123",
            database="Inventario"
        )

        cursor = mydb.cursor()

        # Consulta
        sql = "SELECT nombre, precio FROM productos WHERE código = %s"
        # Nota: la coma es obligatoria en SQL para convertir la variable en tupla
        valor = (datos,) 

        cursor.execute(sql, valor)

        resultado = cursor.fetchone()

        #OUTPUT USUARIO
        output.config(text=resultado) #el texto de esta etiqueta cambia a "resultado"

    
#########INTERFAZ USUARIO###########

import tkinter as tk

ventana = tk.Tk()

entrada = tk.Entry(ventana)
entrada.pack()

tk.Button(ventana, text="Aceptar", command=codigo).pack()

output = tk.Label(ventana, text="Producto: ")
output.pack()

ventana.mainloop()