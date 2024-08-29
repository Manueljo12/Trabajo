n = int(input("Ingrese un valor por favor que sea mayor a 1: "))
x = 0
y = 1
z = 1
while z <= n:
    if z % 2 == 1:
      print(x, end=",")
      x += y
    else:
      print(y, end=",")
      y += x
    z += 1