menu = """
Bienvenido al conversor de moneda 😎

1 - Pesos Uruguayos
2 - Pesos Argentinos
3 - Pesos Colombianos

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("Cuantos pesos Uruguayos tienes: ")
    pesos = float(pesos)
    valor_dolar = 40
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 2:
    pesos = input("Cuantos pesos Argentinos tienes: ")
    pesos = float(pesos)
    valor_dolar = 400
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 3:
    pesos = input("Cuantos pesos Colombianos tienes: ")
    pesos = float(pesos)
    valor_dolar = 3775
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
else:
    print("Entra una opcion correcta")