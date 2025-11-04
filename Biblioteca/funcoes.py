from tabulate import *


def addlivro(lista):
    livro = {
        "titulo" : '',
        "autor" : '',
        "status" : 'DISPONÍVEL'
    }
    
    livro["titulo"] = input("Digite o titulo do livro: ").strip().lower()
    livro["autor"] = input("Digite o titulo do livro: ").strip().lower()
    
    lista.append(livro)
    return lista
    
def emprestarlivro(biblioteca):
    titulos = [livro['titulo'] for livro in biblioteca]
    while True:
        titulo = input('Digite o titulo do livro: ').strip()
        if titulo not in titulos:
            print('Livro não encontrado')
            continue
        break
    pos = titulos.index(titulo)
    biblioteca[pos]['status'] = 'EMPRESTADO'
    return biblioteca


def devolverlivro(biblioteca):
    titulos = [livro['titulo'] for livro in biblioteca]
    while True:
        titulo = input('Digite o titulo do livro: ').strip()
        if titulo not in titulos:
            print('Livro não encontrado')
            continue
        break
    pos = titulos.index(titulo)
    biblioteca[pos]['status'] = 'DISPONIVEL'
    return biblioteca


def exibir(biblioteca):
    print(tabulate(biblioteca, headers='keys', tablefmt='fancy_grid'))

