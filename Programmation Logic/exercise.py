#region exercise 1 
#1. Build a program that asks for a number and then says if this number is even or not?
print("Ingrese un número:")
num=int(input())

import module
if module.modulo(num) == 0:
    print("El número {0} es par".format(num))
else:
    print("El número {0} es impar".format(num))
#endregion

#region exercise 2
#2. Build a program that asks for 3 numbers on the screen and then say which is the largest of the numbers entered?
print("Ingrese tres numeros:")
num1=int(input())
num2=int(input())
num3=int(input())

from module import bigger_number
print("El mayor de los tres números es {0}".format(bigger_number(num1,num2,num3)))
#endregion

#region exercise 3
#3. Build a program that asks for 3 numbers on the screen and then says phones is the largest, the middle one and the smallest of the entered numbers
print("Ingrese tres numeros:")
num1=int(input())
num2=int(input())
num3=int(input())

from module import order
print("{0}".format(order(num1,num2,num3)))
#endregion

#region exercise 4
#4. Build a program that asks for two numbers and says if the second is a multiple of the first.
print("Ingrese el primer número: ")
num1=int(input())
print("Ingrese el segundo número: ")
num2=int(input())

from module import multiple
if multiple(num1,num2) == 0:
    print("El número: {1}, es múltiplo de: {0}".format(num1,num2))
else:
    print("El número: {1}, no es múltiplo de: {0}".format(num1,num2))
#endregion

#region exercise 5
#5. Build a program that asks for a year and then determine if the year is leap or not.
print("Ingrese el año: ")
num=int(input())

from module import year_leap
print(year_leap(num))
#endregion

#region exercise 6
#6. Develop a program that enters the name of an employee, his basic hourly wage and the number of hours worked in the month; Write your name and monthly salary if it is higher than the minimum wage, otherwise write only the name.
print("Ingrese nombre: ")
name=input()
print("Ingrese número de horas trabajadas: ")
h=int(input())
print("Ingrese valor hora: ")
valorh=int(input())
print("Ingrese valor salario mínimo mensual: ")
mini=int(input())

from module import payroll
print(payroll(name,h,valorh,mini))
#endregion

#region exercise 7
#7. A desktop store makes the following discounts: if the customer purchases less than 5 units, a 10% discount on the purchase is granted; if the number of units is greater than or equal to five but less than 10, 20% and, if there are 10 or more, it is given 40%.

print("Número de escritorios: ")
units=int(input())

from module import discount
print(discount(units))
#endregion

#region exercise 8
#8. You want to obtain the value of the enrollment of a student whose value is calculated as follows in a subprogram:
#• If you take 20 or fewer credits, you pay the credit at normal value.
#• If you take more than 20 credits, the extra credits will be paid twice the normal value.
#• If the student is from stratum 1, 2 or 3, he receives the following discounts:
#If the stratum is 1, the discount is 80%.
#If the stratum is 2, the discount is 50%.
#If the stratum is 3, the discount is 30%.
#Furthermore, strata 1 and 2 receive food and transportation subsidy as follows (which must be calculated in another applet):
#• For stratum 1, the food and transportation subsidy is equal to $ 200,000.
#• For stratum 2, the food and transportation subsidy is equal to $ 100,000.
#The user must be informed about the cost of tuition and the value of the subsidy.
print("Ingrese el número de creditos: ")
credit=int(input())

print("Ingrese el valor por credito: ")
value=int(input())

print("Ingrese el estrato desl estudiante: ")
stratum=int(input())

from module import value_credit
print("Costo de la matricula: {0} ".format(value_credit(credit, value, stratum)))
from module import subsidy
print("Valor del subsidio: {0} ".format(subsidy(stratum)))
#endregion