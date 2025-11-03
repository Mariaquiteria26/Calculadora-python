def calcular_media(lista):
    return sum(lista)/len(lista)

def verificar_media(media):
    if media > 7:
        return 'APROVADO'
    elif media < 5:
        return 'REPROVADO'
    else:
        return 'RECUPERAÇÃO'
