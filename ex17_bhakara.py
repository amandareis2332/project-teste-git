print("Bhaskara")
a = float(input("Informe o coeficiente a "))
b = float(input("Informe o coeficiente b"))
c = float(input("Informe o coeficiente c"))

delta = ((b ** 2) - (4*a*c))

if a == 0:
    print("o valor de a tem que ser diferente de 0")
elif delta < 0:
    print("A equação não possui zeros")
else:
    x1 =  (-b + delta ** (1/2)) / (2*a)
    x1 =  (-b - delta ** (1/2)) / (2*a)

    print("x1", x1)
    print("x2", x2)
