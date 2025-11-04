from funcoes import *

lista = []
while True:
    print('''
[ 1 ] ADICIONAR LIVRO
[ 2 ] EXIBIR LIVRO
[ 3 ] EMPRESTAR LIVRO
[ 4 ] DEVOLVER LIVRO
[ 0 ] SAIR
    ''')
    while True:
        op = input('Escolha uma opção: ').strip()
        if op not in ['1', '2', '3', '4', '0']:
            print('Opção inválida ')
            continue
        break
    
    if op == '0':
        break
    elif op == '1':
        lista = addlivro(lista)
    elif op == '2':
        exibir(lista)
    elif op == '3':
        lista = emprestarlivro(lista)
    elif op == '4':
        lista = addlivro(lista)
    
    