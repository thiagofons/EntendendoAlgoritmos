def main():
    lista = [1, 2, 3, 4, 5, 6]

    print(soma(lista))

    return 0

def soma(lista):
    if not lista:
        return 0
    return lista[0] + soma(lista[1:])

main()

