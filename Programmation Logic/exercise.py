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

#region exercise 9
#9. A merchandise shipping company has a rate and discount plan on the value of its clients' merchandise shipment:
#• Rates:
#If the weight of the merchandise is less than 100 kg, the rate for its shipment is 20,000 pesos.
#If the weight of the merchandise is between 100 and 150 kg, the rate for its shipment is 25,000 pesos.
#If the weight of the merchandise is greater than 150 kg and less than or equal to 200 kg, the rate for its shipment is 30,000 pesos.
#If the weight of the merchandise is over 200 kg, the fee is 35,000 pesos and also for each additional 10 kg you pay 2,000 pesos.
#• Discounts:
#If the value of the merchandise is between 300,000 and 600,000 pesos, a 10% discount is made on the value of the shipment.
#If the value of the merchandise is greater than 600,000 but less than or equal to 1,000,000 pesos, a 20% discount is made. about the shipping value.
#If the value of the merchandise is greater than 1,000,000, a 30% discount is made on the value of the shipment.
#• Promotions (there are only two types of payment):
#If it is a promotion day (Monday) and you pay with your own store card, you only pay 50% of the shipping cost.
#If you pay in cash and the value of the merchandise is over 1,000,000, you only pay 60% of the shipping cost.
#If the customer applies to a promotion, they cannot apply to a discount. The full value of the shipment must be obtained.
print("Ingrese Peso de la mercancía: ")
weigh=int(input())
print("Ingrese Valor de la mercancía: ")
merchandise_value=int(input())
print("Es lunes [S]í [N]o: ")
monday=input()
print("Tipo de pago [E]fectivo [T]arjeta: ")
payment_type=input()

print("Peso de la mercancía: {0}".format(weigh))
print("Valor de la mercancía: {0}".format(merchandise_value))
print("Es lunes [S]í [N]o: {0}".format(monday))
print("Tipo de pago [E]fectivo [T]arjeta: {0}".format(payment_type))
from module import tariff
print("Tarifa: {0}".format(tariff(payment_type, monday, merchandise_value, weigh)))
from module import promotion
if promotion(payment_type, monday, merchandise_value, weigh)>0:
    print("Promoción: {0}".format(promotion(payment_type, monday, merchandise_value, weigh)))
from module import discounts
if discounts(payment_type, monday, merchandise_value, weigh)>0:
    print("Descuento: {0}".format(discounts(payment_type, monday, merchandise_value, weigh)))

from module import total
total(payment_type, monday, merchandise_value, weigh)
#endregion