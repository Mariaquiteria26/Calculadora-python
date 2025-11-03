from operacoes import *


def menu():
    while True:
        try:
            n1 = int(input("Digite o primeiro número: "))
            n2 = int(input("Digite o segundo número: "))
            break
        except ValueError:
            print("Erro, número ivalido!")
    print('''
OPÇÕES:
    [1] Adição
    [2] Subtração
    [3] Multiplicação
    [4] Divisão
    [0] SAIR
''')
    while True:
        op = input("Escolha uma opção ")
        if op not in ["0", "1", "2", "3","4"]:
            print("Erro: opção inexistente")
            continue
        break
    return op, n1, n2


def opcs(op, n1, n2):
    if op == '1':
        resultado = soma(n1, n2)
    elif op == '2':
        resultado = subtração(n1, n2)
    elif op == '3':
        resultado = multiplicação(n1, n2)
    elif op == '4':
        resultado = divisão(n1, n2)
    return resultado


def main():
    op, a, b = menu()
    if op == '0':
        return
    result = opcs(op, a, b)
    print(f'Resultado: {result}')


main()
