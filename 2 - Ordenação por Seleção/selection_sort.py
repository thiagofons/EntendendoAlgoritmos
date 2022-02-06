def main():
    arr = []

    print("Insira os elementos do array: ", end="")
    arr = list(map(int, input().split()))
    arr = selectionSort(arr)

    print("\nArray ordenado: ", end="")
    for i in range(len(arr)):
        print(arr[i], end=" ")
        
    return 0

def buscaMenor(arr):
    menor = 0
    for i in range(len(arr)):
        if arr[i] < arr[menor]:
            menor = i
    return menor

def selectionSort(arr):
    novoArr = []

    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))

    return novoArr

main()