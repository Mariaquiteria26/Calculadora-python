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
    
