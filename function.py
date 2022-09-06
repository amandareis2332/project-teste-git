#def boasvidas():
#    print("Olá Marcos!")
#    print("Temos 5 laptops em estoque")

#boasvidas()

#print("Olá Marcos!")
#print("Olá Marcos!")
#print("Olá Marcos!")
#print("Olá Marcos!")
#print("Olá Marcos!")

#boasvidas()

 
#somar dois numeros
#def somardoisnumeros():
#    number1 = 10
#    number2 = 5
#    result = number1 + number2
#    print(result)

#def somardoisnumeros1():
#    number1 = 10
#    number2 = 12
#        result = number1 + number2
#    print(result)


#somardoisnumeros ()
#somardoisnumeros1 ()

'''

def boasvidasMarcos():
    print("Olá Marcos!")
    print("Temos 4 laptops em estoque")

def boasvidasronaldo():
    print("Olá Ronaldo!")
    print("Temos 2 laptops em estoque")

def boasvidasgabi():
    print("Olá Gabi!")
    print("Temos 1 laptops em estoque") 

boasvidasMarcos()
boasvidasronaldo()
boasvidasgabi()

''' 
'''
#parametros --> argumentos
def boasvindas(nome, quantidade):
    print(f"Ola {nome}.")
    print(f"Temos {str(quantidade)} em estoque.")

boasvindas("Marcos", 5)
boasvindas("Ronaldo", 2)
boasvindas("Gabi", 1)
'''

'''
#default tem que ter ordem 
#se quiser definir um parametro voce tem que definir no final
#Default = aquele que você definiu o valor no parametros
#Non-Default = aquele que voce não define o valor no parametro


def boasvindas(nome, quantidade=6):
    print(f"Ola {nome}.")
    print(f"Temos {str(quantidade)} em estoque.")

boasvindas("marcos")
'''


'''
#o * no inicio significa que posso colocar varios que podem entrar la
# não tem um numero definido
def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado

x = soma(2,3,4,7)
print(x)

def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado -= num
    return resultado

x = sub(*numeros)
print(x)
'''

#dois * significa que posso passar varios parametros dentro de um dic
#agora posso definir os paramentro que eu quiser sem ter que alterar o parametro na parte superior
'''
def agencia(**carro):
    return carro

print(agencia(marca="gol",cor= "Branca",motor= 1.0, placa= 1234))
print(agencia(marca="gol",cor= "Preto",motor= 1.3, placa= 4444))
'''

#numeros fatoriais
#Qual é o numero fatorial de 4? 4X3X2X1 = 24
#como fazer isso em python

#fatorial = 4*3*2*1
#print(fatorial)
#importar o modo math

#import math
#print(math.factorial(4))

import math
print(math.floor(2,7))




