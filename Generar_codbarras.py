
import barcode
from barcode.writer import ImageWriter

CODABAR = barcode.get_barcode_class('codabar')

for i in range (1): # seteado en "1" para que itere solo 1 vez. El output será "A0A". Nota: range(i, j) produces i, i+1, i+2, ..., j-1
 serie = "A" + str(i) + "A"
 codigo = CODABAR(serie, writer=ImageWriter())
 codigo.save(serie) #si el script se ejecuta en una carpeta específica los códigos quedan guardados en esa carpeta