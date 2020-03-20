def modulo(num):
    return num%2

def bigger_number(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        n=num1
        return n
    else:
        if num2>=num1 and num2>=num3:
            n=num2
            return n
        else:
            n=num3
            return n
        
def order (num1,num2,num3):
    a = min(num1,num2,num3)
    c = max(num1,num2,num3)
    b = (num1+num2+num3)-a-c
    e = "El número mayor es: {0}\nEl número del medio es: {1}\nEl número menor es: {2}".format(c,b,a)
    return e

def multiple(num1,num2):
    return num1%num2

def year_leap(num):
    if (num%4==0 and num%100!=0) or (num%400==0):
        return "El año: {0}, si es biciesto".format(num)
    else:
        if (num%4==0) and (num%100!=num or num%400):
            return "El año: {0}, si es biciesto".format(num)
        else:
            return "El año: {0}, no es biciesto".format(num)
        
def payroll(name,h,valorh,mini):
    valor=valorh*h  
    if valor>mini:
        return "Nombre: {0}\nSalario Mensual: {1}".format(name,valor)
    else:
        return "Nombre: {0}".format(name)

def discount(units):
    valor_compra=650000*units
    if units<5:
        valor_total=valor_compra-(valor_compra*0.1)
        return "El valor a pagar es: {0}".format(valor_total)
    else:
        if units>=5 and units<10:
            valor_total=valor_compra-(valor_compra*0.2)
            return "El valor a pagar es: {0}".format(valor_total)
        else:
            if units>=10:
                valor_total=valor_compra-(valor_compra*.4)
                return "El valor a pagar es: {0}".format(valor_total)

def value_credit(credit, value, stratum):
    if stratum==1:
        percentage=0.8
    else:
        if stratum==2:
            percentage=0.5
        else:
            if stratum==3:
                percentage=0.3
            else:
                percentage=0.0

    if credit<20:
        return (credit*value)*percentage
    else:
        return ((value*20)+((credit-20)*value*2))*percentage

def subsidy(stratum):
    if stratum==1:
        return 200000
    else:
        if stratum==2:
            return 100000