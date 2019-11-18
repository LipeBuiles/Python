3
10.1
print(type(3))
print(type(10.1))
print(3+10.1)

# Raise an exponent
print(2**10)

# Divide
print(10/3)
print(10//3)

# Module (you can get the residue)
print(10 % 3)

# Example
a = int(input("Ingrese el dividendo: "))
b = int(input("Ingrese el divisor: "))
c = a//b
d = a % b
print("La división entre {0} y {1} generá como cociente {2} y residuo {3}".format(
    a, b, c, d))
