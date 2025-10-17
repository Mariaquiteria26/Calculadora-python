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
CALCULADORA PYTHON  - por Lohane & Quitéria
          
OPÇÕES:
    [1] Adição
    [2] Subtração
    [3] Multiplicação
    [4] Divisão
    [0] SAIR
''')
    while True:
        op = input("Escolha uma opção ")
        if op not in["0", "1", "2", "3","4"]:
            print("Erro: opção inexistente")
