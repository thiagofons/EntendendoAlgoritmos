def main():
    lista = [1, 2, 3, 4, 5, 6, 4, 7, 12, 3]

    print(maior(lista))

    return 0


def maior(lista):
    if not lista:
        return 0
    else:
        if(lista[0] > maior(lista[1:])):
            return lista[0]
        else:
            return maior(lista[1:])

main()