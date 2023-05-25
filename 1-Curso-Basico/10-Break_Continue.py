def run():
    # for contador in range(10):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # for i in range(100):
    #     print(i)
    #     if i == 87:
    #         break

    texto = input("Escribe un texto: ")
    for i in texto:
        if i == 'a':
            break
        print(i)


if __name__ == '__main__':
    run()