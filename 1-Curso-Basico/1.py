#Guardamos en la variable dolar lo que entra el user por pantalla
pesos = input("Cuantos pesos uruguayos tienes: ")

#Convertir la var dolar a tipo flotante
pesos = float(pesos)

valor_dolar = 40
dolares = pesos / valor_dolar

#Aqui tomamos solo los 2 primeros caracteres despues de la coma
dolares = round(dolares, 2)

#Convertimos la variable dolar a texto para poderla imprimir
dolares = str(dolares)

#Imprimir el valor
print("Tienes $" + dolares + " dolares")