pesos = int(input("Cuantos pesos tienes "))
soles = int(input("Cuantos soles tienes "))
reales = int(input("Cuantos reales tienes "))

pesos_a_dolar = float(pesos*0.00025)
soles_a_dolar = float(soles*0.27)
reales_a_dolar = float(reales*0.18)

dolares = (pesos_a_dolar+soles_a_dolar+reales_a_dolar)
print ("Su saldo en dolares es de $",dolares)