#resolução ex01 lista01

numero = 1
print(type(numero))

numero = 12.6
print(type(numero))

comida = True
print(type(comida))

bebida = False
print(type(bebida))

numero = -543
print(type(numero))

numero = -5.78
print(type(numero))

objeto = "copo"
print(type(objeto))

frase = 'Belo dia'
print(type(frase))

#resolução ex02 lista01
#1
#a1
#NameError: name 'a1' is not defined
#1.
#.2
#-.3
#'agua"limpa'
#"agua"
#erro de aspas
#"""teste 1 2 3"""

#resolução ex03(a)lista01
#a) math operator, ternary operator, logic operator
#ai. resultado 10+3
x = 10
y = 3
calculo = x + y
print(calculo)

#aii. resultado 10-3
calculo2 = x - y
print(calculo2)

#aiii. resultado 30
calculo3 = x * y
print(calculo3)

#aiv resultado 10/3
calculo4 = x / y
print(calculo4)

#av. resultado 10 / 3.0
calculo5 = int(x) / float(y)
print(calculo5)

#avi. resultado 13 / 3
calculo6 = ((x + y ) / y)
print(calculo6)

#avii resultado 13 / 3.0
calculo7 = ((x + y) / float(y))
print(calculo7)

#aviii. 13//3.0
calculo8 = ((x+y) // float(y))
print(calculo8)


#resolução ex03(b)lista01
a = 5
b = 30
c = 20
d = 10

#bi 5 + 30 * 20 = 605
result1 = a + b * c
print(result1)

#bii. (5 + 30) * 20 = 700
result2 = ((a+b) * c)
print(result2)

#biii. ((5 + 30) * 20) / 10 = 70
result3 = (((a+b)*c )/ d)
print(result3)

#ci. 2 < 3
dois = 2
tres = 3
if dois < tres:
    print("ok")
else:
    print("Não")

nove = 9
oito = 8
if nove > 8:
    print("ok")
else:
    print("Não")

um = 1
if um == um:
    print("São iguais")
else:
    print("Não")

if um!=dois:
    print ("São diferentes")
else:
    print("São iguais")

if um != um:
    print("São diferentes")
else:
    print("São iguais")

quatro = 4
if quatro <= quatro:
    print(True)
else:
    print(False)

cinco = 5
seis = 6

if cinco >= seis:
    print(True)
else:
    print(False)


if dois > um and dois < 3:
    print("Verdadeiro")
else:
    print("Não é verdade")


if dois > um and dois < dois:
    print("verdadeiro")
else:
    print("não é verdadeiro")

f = 25
resultado = ((um + dois) / f/cinco)
print(resultado)

#d mais operadores logicos
calculo1 = dois ** quatro
print(calculo1)

g = 26
calculo2 = g % cinco
print(calculo2)

#RESOLUÇÃO EX04-LISTA01
#x=10
#x=x+10
#print(x)
#coloquei como comentario para não alterar o resultado de x

cem = 100
x = cem - x
print(x)

#RESOLUÇÃO EXERCICIO 5.A) resultado 4
lado = 2
areaquad = lado * lado
print(areaquad)

#RESOLUÇÃO EXERCICIO 5.A) resultado 114.0
mala = 120.0
malacomdes = mala * 0.95
print(malacomdes)

#RESOLUÇÃO EXERCICIO 5. B) resultado 2.0 horas
velocidade = 100
distancia = 200
tempo = distancia/velocidade
print(tempo, "horas")

#RESOLUÇÃO EXERCICIO 5. C) resultado 6 
joao = 2
maria = 3
sofia = 1
somapirulitos = joao + maria + sofia
print(somapirulitos)

#RESOLUÇÃO EXERCICIO 5. D) 
idadedavi = 13
idadeirma = 7
if idadedavi > idadeirma:
    print("eh_mais_velho")


#RESOLUÇÃO EXERCICIO 6  - resultado 5
z = 3
z +=2
print(z)

z *= 6 #resultado 30
print(z)

z /= 5
print(z) #resultado 6.0


#RESOLUÇÃO EXERCICIO 7

ovo = 3.4
caju = 12.4
resposta = ovo if 1 > 2 else caju
print(resposta) #resposta 12.4

resposta = ovo if ovo > caju else caju
print(resposta) #resposta 12.4

resposta = ovo if ovo < caju else caju
print(resposta) #resposta 3.4

resposta = 100 if ovo + caju > 15 else 200
print(resposta) #resposta 100

resposta = 100 if ovo == 3 else 0
print(resposta) #resposta 0

#RESOLUÇÃO EXERCICIO 7
ab = 10
Ab = 20
aB = 30
AB = ab + Ab - aB
print(AB) #resposta 0

fim = AB + 1
print(fim) #resposta 1

#RESOLUÇÃO EXERCICIO 9
valor = input("Informe um valor: ")
print(valor)
#pede para informar um valor

print("Valor informado: ", valor)
#Valor informado: (o valor que eu coloquei)

tipo = type(valor)
print(tipo) #tipo = type(valor)

x_str = "123"
print(x_str) #resultado123 string

x = int(x)
print(x) #aparece o ultimo resultado que usei para x como int

xf = float(x)
print(xf) #APARECE X COMO FLOAT

sao_iguais = x == xf

print("Um float é igual a um int?", sao_iguais)














