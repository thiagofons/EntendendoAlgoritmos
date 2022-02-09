def main():
    vetor = list(map(int, input("Insira o vetor: ").split()))

    print("\nVetor Ordenado: ", quicksort(vetor))

    return 0

def quicksort(array):
    if len(array) < 2:
        return array
    
    pivo = array[0]
    menores = [i for i in array[1:] if i <= pivo]
    maiores = [i for i in array[1:] if i > pivo]

    return quicksort(menores) + [pivo] + quicksort(maiores)

main()