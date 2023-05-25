def operacion(numero1, numero2, simbolo, opcion):
    contador = 1
    while contador < numero1:
        print('\n💛\n')
        contador += 1
    print('\n{}\n'.format(simbolo))
    contador = 1
    while contador < numero2:
        print('\n💛\n')
        contador += 1
    
    if simbolo == '+':
        result = numero1 + numero2
    elif simbolo == '-':
        result = numero1 - numero2
    
    numero = int(input('\nEscribe el resultado de la {}: '.format(opcion)))
    while(numero != result):
        numero = int(input('\nEscribe el resultado correcto de la {}: '.format(opcion)))
        continue
    print('\Es correcto el resultado de la {} es {}. Felicitaciones ... 💛🧡❤✅✅❎'.format(opcion))


def run():
    menu = """

    Bienvenido al juego para sumar y restar

    Para suma, escribe 1...
    Para restar, escribe 2...

    Elige una opcion

    """

    opcion = int(input(menu))

    while opcion != 1 and opcion != 2:
        print('\n Ingresa una opcion correcta\n')
        opcion = input(menu())
        continue
    numero1 = int(input('\nEscribe el primer numero\n'))
    numero2 = int(input('\nEscribe el segundo numero\n'))
    if opcion == 1:
        operacion(numero1, numero2, '+', 'suma')
    elif opcion == 2:
        while numero1 < numero2:
            print('\nLo siente no pouede restar ahora, el primer numero deber ser mayor. Vuelve a intentarlo \n')
            numero1 = int(input('\nEscribe el primer numero\n'))
            numero2 = int(input('\nEscribe el segundo numero\n'))
            continue
        operacion(numero1, numero2, '-', 'resta')
    else:
        print('\nNinguna opcion es correcta\n')


if __name__ == "__main__":
    run()