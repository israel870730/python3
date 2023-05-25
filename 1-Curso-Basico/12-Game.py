import random

def run():
    numerorandom = random.randint(1, 100)
    print('Tienes solo 5 opciones')
    numeroelegido = int(input("Introduce un numero: "))
    print(numerorandom)
    vidas = 5
    
    while numerorandom != numeroelegido:
        if numerorandom < numeroelegido: 
            print("Elige un numero mas pequeño.")
            numeroelegido = int(input("Introduce un nuevo numero: "))
            vidas -= 1
            str(vidas)
            print("Tienes", vidas, "vidas")
        else:
            print("Elige un numero mas grande.")
            numeroelegido = int(input("Introduce un nuevo numero: "))
            vidas -= 1
            print("Tienes", vidas, "vidas")
        
    print("Victoria")


if __name__ == "__main__" : 
    run()



# import random

# def run():
#     numerorandom = random.randint(1, 100)
#     numeroelegido = int(input("Introduce un numero: "))
#     vidas = 5
#     while numerorandom != numeroelegido :
#         if numerorandom < numeroelegido : 
#             print("Elige un numero mas pequeño.")
#             vidas -= 1
#         elif numerorandom > numeroelegido : 
#             print("Elige un numero mas grande.")
#             vidas -= 1
#         if vidas == 0 :
#             print("GAME OVER")
#             break
#         print("Tienes", vidas, "vidas")
#         numeroelegido = int(input("Introduce numero: "))
#     if numerorandom == numeroelegido : 
#         print("FELICIDADES GANASTE")


# if __name__ == "__main__" : 
#     run()