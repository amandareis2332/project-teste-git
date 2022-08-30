print("Bhaskara")
a = input("Informe o coeficiente a")
b = input("Informe o coeficiente b")
c = input("Informe o coeficiente c")
a = (int(a))
b = (int(b))
c = (int(c))

delta = ((b ** 2) - (4*a*c))
delta = float(delta)
x1 = ((-b + raizquadr1(delta)) / (2*a))
x2 = ((-b - raizquadr(delta)) / (2*a))
if a == 0 or delta < 0:
    print("A equação não possui zeros")
else:
    print("x1=", x1 + "x2= ", x2)