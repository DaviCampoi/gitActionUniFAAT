def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def subtracao(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b

def potencia(a, b):
    return a ** b

if __name__ == "__main__":
    a = 10
    b = 5

    print("Soma:", soma(a, b))
    print("Subtração:", subtrai(a, b))
    print("Multiplicação:", multiplica(a, b))
    print("Divisão:", divide(a, b))
    print("Potenciação:", potencia(a, b))
