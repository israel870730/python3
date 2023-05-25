#Guardamos en la variable dolar lo que entra el user por pantalla
dolar = input("Cuantos dolares tienes: ")

#Convertir la var dolar a tipo flotante
dolar = float(dolar)

valor_dolar = 40
pesos = dolar * valor_dolar

#Aqui tomamos solo los 2 primeros caracteres despues de la coma
pesos = round(pesos, 2)

#Convertimos la variable dolar a texto para poderla imprimir
pesos = str(pesos)

#Imprimir el valor
print("Tienes $" + pesos + " dolares")