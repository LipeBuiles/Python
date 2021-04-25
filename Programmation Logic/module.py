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

def tariff(payment_type, monday, merchandise_value, weigh):
    import math
    if weigh<100:
        shipping_fee=20000
        return shipping_fee
    else:
        if weigh>=100 and weigh<=150:
            shipping_fee=25000
            return shipping_fee
        else:
            if weigh>=150 and weigh<=200:
                shipping_fee=30000
                return shipping_fee
            else:
                shipping_fee=35000+(math.floor(((weigh-200)/10))*2000)
                return shipping_fee

def promotion(payment_type, monday, merchandise_value, weigh):
    shipping_fee=tariff(payment_type, monday, merchandise_value, weigh)
    if(monday=='S' or monday=='s') and (payment_type=='T' or payment_type=='t'):
        shipping_fee=shipping_fee*0.50
        return int(shipping_fee)
    else:
        if (payment_type=='E' or payment_type=='e') and shipping_fee>1000000:
            shipping_fee=shipping_fee*0.60
            return int(shipping_fee)
        else:
            shipping_fee=0
            return int(shipping_fee)

def discounts(payment_type, monday, merchandise_value, weigh):
    shipping_fee=promotion(payment_type, monday, merchandise_value, weigh)
    tariff1=tariff(payment_type, monday, merchandise_value, weigh)
    if shipping_fee==0.00:
        if merchandise_value>=300000 and merchandise_value<=600000:
            shipping_fee=tariff1*0.1
            return int(shipping_fee)
        else:
            if merchandise_value>=600000 and merchandise_value<=1000000:
                shipping_fee=tariff1*0.2
                return int(shipping_fee)
            else:
                if merchandise_value>1000000:
                    shipping_fee=tariff1*0.3
                    return int(shipping_fee)
                                
    else:
        shipping_fee=0
        return int(shipping_fee)

def total(payment_type, monday, merchandise_value, weigh):
    a=int(tariff(payment_type, monday, merchandise_value, weigh))
    b=int(promotion(payment_type, monday, merchandise_value, weigh))
    c=int(discounts(payment_type, monday, merchandise_value, weigh))
    d=a-b-c
    return print("Total a pagar: {0}".format(d))

def almacenes_suceso(CC, TP, TC, PC, PA, VOL, MA):
    if PA<30:
        PDP=0.95
    if PA>=30:
        PDP=0.85

    if TP=='P' or TP=='p':
        if (TC=='F' or TC=='f') and (PC<10):
            CA=CC*0.05
        if (TC=='F' or TC=='f') and (PC>=10):
            CA=CC*0.10
        if (TC=='A' or TC=='a') and (PC<20):
            CA=CC*0.03
        if (TC=='A' or TC=='a') and (PC>20):
            CA=CC*0.10
        if (TC=='A'or TC=='a') and (PC==20):
            CA=CC*0.05

    if TP=='N' or TP=='n':
        if VOL>=50:
            CA=CC*0.10
        if VOL<50:
            CA=CC*0.20

    if TP=='P' or TP=='p':
        if (TC=='F' or TC=='f') and (MA=='N' or MA=='n'):
            CE=CA*2
        if (TC=='F' or TC=='f') and (MA=='C' or MA=='c'):
            CE=CA

    if TP=='N' or TP=='n':
        if MA=='E' or MA=='e':
            CE=CA*0.05
        if MA=='G' or MA=='g':
            CE=CA*0.07
    
    VR_P=(CC+CA+CE)*PDP

    if TP=='P' or TP=='p':
        VR_V=VR_P+VR_P*0.40
    if TP=='N' or TP=='n':
        VR_V=VR_P+VR_P*0.20

    return CA, PDP, CE, VR_P, VR_V