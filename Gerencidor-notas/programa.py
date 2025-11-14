from funcoes import *
from pandas import *

lista = []

while True: 
    print('''
[1] Cadastrar aluno e notas
[2] Exibir relatório
[0] Sair
''')

    while True:
        dicio = {
        'nome'  : '',
        'notas' : [],
        'media' : 0
        }
        op = input("escolha a sua opção: ")
        if op not in ['0', '1', '2']:
            print("opção inválida")
            continue
        break
    
    if op == '0':
        break
    
    elif op == '1':
        notas = []
        nome = input("digite o nome do aluno: ")
        
        for i in range(3):
            while True:
                notas.append(int(input(f"digite a {i+1}ª nota: ")))
                break
                    
        dicio['nome'] = nome
        dicio['notas'] = notas
        dicio['media'] = calcular_media(notas)
        lista.append(dicio)
        
    elif op == '2':
        tabela = DataFrame(lista)
        print(tabela)
