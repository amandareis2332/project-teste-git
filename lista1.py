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
    
