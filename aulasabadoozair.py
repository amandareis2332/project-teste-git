#EXEMPLO LISTA  
'''
lista = [1,2,3,4,5,6,7,8,9]
soma = 0
soma = sum(lista)
print("Resultado", soma)
'''

#primeiro modo de somar elementos pares da lista
'''
lista = [1,2,3,4,5,6,7,8,9]

soma = 0
for valor in lista:
    if valor%2 == 0:
        soma = soma + valor
    continue

print(soma)
'''
'''
#segundo modo de soma elementos pares da lista
lista = [1,2,3,4,5,6,7,8,9]
soma = 0
for valor in lista:
    if valor%2 != 0:
        continue
    soma = valor + soma

print(soma)
'''

#LISTA INDEXADA
'''
lista = [1,2,3,4]
x = lista[0]
print(x)
'''
#DICIONARIO
'''
dicionario = {}
dicionario = {
    1: "amanda",
    2:"jeferson",
    3:"gabi"
}
print("dicionario chaves numericas", dicionario)
print ("chave3", dicionario[3])
print(dicionario)
etiqueta = 4
existechave4 = etiqueta in dicionario
if existechave4:
    print("chave5" , dicionario[5])
else:
    print("nao existe")


#tentar pegar a chave 4 (get)
valorchave4 = dicionario.get(etiqueta)
print(chave4)
'''
#funções
def lernumeros():
    lista = [1,2,3,4,5,6,7,8,9]
    return lista
    print(lernumeros(0))

soma = 0

def somarlista(lista):
    soma = sum(lista)
    return soma

def mostrarresultado(soma):
    print("resultado", soma)
