def contadoraVogais(palavra:str):
    vogais = "aeiou"
    contador = 0 


    for letra_da_vez in palavra:
        if letra_da_vez in vogais:
            contador += 1
    return contador



def contadoracosoantes(palavra:str):
    cosoantes = "bcdfghjklmnpqrstvwyz"
    contador = 0
    for letra_da_vez in cosoantes:
        if letra_da_vez in palavra:
            contador += 1
    return contador


def contadorarmaiscula(palavra:str):
    return palavra.lower()


def contadoraminusculo(palavra:str):
    return palavra.upper()


def contarFrase(frase:str):
    
    contador = 1
    for palavra_da_vez in frase:
        if palavra_da_vez in " ":
            contador += 1

    return contador