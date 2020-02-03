#1. Build a program that asks for a number and then says if this number is even or not?
print("Ingrese un número:")
num=int(input())

import module
if module.modulo(num) == 0:
    print("El número {0} es par".format(num))
else:
    print("El número {0} es impar".format(num))

#2. Build a program that asks for 3 numbers on the screen and then say which is the largest of the numbers entered?
print("Ingrese tres numeros:")
num1=int(input())
num2=int(input())
num3=int(input())

from module import bigger_number
print("El mayor de los tres números es {0}".format(bigger_number(num1,num2,num3)))