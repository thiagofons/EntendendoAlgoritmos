def main():
    lista = [1, 2, 3, 4, 5, 6]

    print(conta(lista))

    return 0

def conta(lista):
    if not lista:
        return 0
    return 1 + conta(lista[1:])
    
main()