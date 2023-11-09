import string
lista = string.ascii_lowercase + string.ascii_uppercase+ string.digits + string.punctuation + ' '

#função para cifrar
def cifrar(frase, chave):
    cifra = ""
    chave_atual = [int(chave[i]) for i in range(3)]

    for char in frase:
        index = lista.index(char)
        index += chave_atual[0]
        if index >= len(lista):
            index -= len(lista)
        cifra += lista[index]
        chave_atual = chave_atual[1:] + [chave_atual[0]] 

    return cifra

def decifrar(frase, chave):
    decifra = ""
    chave_atual = [int(chave[i]) for i in range(3)]

    for char in frase:
        index = lista.index(char)
        index -= chave_atual[0]
        if index < 0:
            index += len(lista)
        decifra += lista[index]
        chave_atual = chave_atual[1:] + [chave_atual[0]] 

    return decifra