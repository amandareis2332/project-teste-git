print("Bhaskara")
a = int(input("Informe o coeficiente a "))
b = int(input("Informe o coeficiente b"))
c = int(input("Informe o coeficiente c"))

delta = float((b ** 2) - (4*a*c))
x1 = float((-b + raizquadr1(delta)) / (2*a))
x2 = float((-b - raizquadr(delta)) / (2*a))
if a == 0 or delta < 0:
    print("A equação não possui zeros")
else:
    print("x1= ", x1 + "x2 = ", x2)
    