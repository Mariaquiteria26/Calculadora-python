from funcoes import *


while True:
    print('''
[1] Cadastrar aluno e notas
[2] Exibir relatório
[0] Sair
''')
    
    while True:
        op = input("escolha a sua opção: ")
        if op not in ['0', '1', '2']:
            print("opção inválida")
            continue
        break
    if op == '0':
        break
    elif op == '1':
        listas = notas = []
        nome = input("digite o nome do aluno: ")
        for i in range(3):
            while True:
                try:
                    notas.append(int(input(f"digite a {i+1}ª nota: ")))
                    break
                except ValueError:
                    print("erro, valor inválido.")
