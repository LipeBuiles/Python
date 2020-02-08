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