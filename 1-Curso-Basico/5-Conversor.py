def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cuantos pesos " + tipo_pesos + " tienes: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

menu = """
Bienvenido al conversor de moneda 😎

1 - Pesos Uruguayos
2 - Pesos Argentinos
3 - Pesos Colombianos

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    conversor("Uruguayos", 40)
elif opcion == 2:
    conversor("Argentinos", 400)
elif opcion == 3:
    conversor("Colombianos", 2775)
else:
    print("Entra una opcion correcta")