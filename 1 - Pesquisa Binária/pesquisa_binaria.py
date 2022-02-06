def main():
    lista = list(map(int, input("Insira a lista: ").split()))    
    elem = int(input("Qual elemento voce deseja buscar? "))

    print("Posiçao de {} = {}".format(elem, pesquisa_binaria(lista, elem)))

    return 0

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if(chute == item):
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1

    return None

main()