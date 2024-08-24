tamaño_objeto = int (input("Ingrese el tamaño del objeto "))
umbral = int (input("En que distancia se encuentra el umbral "))

if tamaño_objeto > 10 and umbral < 1000 :
    print ("Se requerira maniobras evasivas")

else :
    print ("El objeto no representa ninguna amenaza")