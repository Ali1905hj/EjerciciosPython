import random 
pregunta= input("Bienvenido a MAGIC 8, cual es tu pregunta?")

num = random.randint (1,9)
if num ==1:
    print ("Si, definitivamente")
elif num ==2:
    print ("Definitivamente es asi")
elif num ==3:
    print ("Sin duda")
elif num ==4:
    print ("Respuesta confusa, intentalo de nuevo")
elif num ==5:
    print ("Vuelve a preguntar mas tarde")
elif num ==6:
    print ("Mejor no te lo digo ahora")
elif num ==7:
    print ("Mis fuentes dicen que no")
elif num ==8:
    print ("Las perspectivas no son muy buenas")
else :
    print ("Muy dudoso")

