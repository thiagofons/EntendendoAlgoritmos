def fatorial(x):
    if x==1 or x==0:
        return 1
    return x * fatorial(x - 1)

def main():
    num = int(input("Insira um numero: "))

    print("\nO fatorial de {} é {}".format(num, fatorial(num)))

    return 0
main()