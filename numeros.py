def verificarnumero(numero):
    if numero % 2 == 0:
        return(f"o numero {numero} é par")
    else:
        return(f"o numero {numero} é impar")


def verificarnumweo(numero):
    if numero == 0:
        return "neutro"
    else:
        return "negativo"

lista = [1,2,3,4,5,6,7,8,9,10]
maior = lista[0]


for lista_da_vez in lista:
    if lista_da_vez > maior:
        maior = lista_da_vez

print(maior)

lista2 = [1,2,3,4,5,6,7,8,9,10]
menor = lista2[0]

for lista_da_vez in lista2:
    if lista_da_vez < menor:
        menor = lista_da_vez

print(menor)

def mediaDosNumeros(lista_de_numeros:list) -> float:
    soma_total = 0
    for numero_da_vez in lista_de_numeros:
        soma_total += numero_da_vez
    media = soma_total / len(lista_de_numeros)
    return media