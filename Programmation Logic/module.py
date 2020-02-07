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