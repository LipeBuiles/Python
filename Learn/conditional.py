x = 40
if x < 30:
    print("la edad x es menor que mi edad")
else:
    print("la edad x es mayor que mi edad")

color = "red"
if color == "blue":
    print("el color es azul")
else:
    print("el color no es azul")

color = "red"
if color == "blue":
    print("el color es azul")
elif color == "red":
    print("el color es rojo")
else:
    print("el color no es azul")

name = "Juan Felipe"
last_name = "Builes"

if name == "Juan Felipe":
    if last_name == "Builes":
        print("Mi nombre es Juan Felipe Builes")
    else:
        print("Mi nombre no es Juan Felipe Builes")
else:
    print("No eres Juam Felipe")

x = 5
if x > 2 and x <= 10:
        print("El número se encuentra entre 2 y  10")
x = 25
if x > 2 or x <= 10:
        print("El número no cumple la condición")
x = 25
y = 24
if (not(x == y)):
        print("Los números X y Y son diferentes")
