altura = int(input("introduzca su altura en centimetros "))
creditos = int(input("Cuantos creditos tiene "))

if altura >= 137 and creditos >= 10 :
    print ("Disfruta el viaje")
elif altura <= 137 and creditos >=10 :
    print ("Lo lamento, no eres lo suficiente alto para viajar")
elif altura >=137 and creditos <=10 :
    print ("No tienes los suficientes creditos")

elif altura < 137 and creditos < 10:
    print ("No cumples con ninguno de los requisitos")