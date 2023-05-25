def main():
    frase = input('Escribe una frase: ')
    frase = frase.replace(' ', '')
    for letra in frase:
        print(letra.upper())    


if __name__ == '__main__':
    main()