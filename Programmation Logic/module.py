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

def comision_pasajero(num_pasajero, ruta, num_viajes):
    if ruta==1:
        if num_pasajero<50:
            comision = 0
        if num_pasajero>=50 and num_pasajero<=100:
            comision = 0.05 * 500000
        if num_pasajero>=101 and num_pasajero<=150:
            comision = 0.06 * 500000
        if num_pasajero>=151 and num_pasajero<=200:
            comision = 0.07 * 500000
        if num_pasajero>200:
            comision = 0.07 * 500000 + (num_pasajero-200) * 50
        return comision

    if ruta==2:
        if num_pasajero<50:
            comision = 0
        if num_pasajero>=50 and num_pasajero<=100:
            comision = 0.07 * 600000 * num_viajes + num_viajes * 600000
        if num_pasajero>=101 and num_pasajero<=150:
            comision = 0.08 * 600000 * num_viajes + num_viajes * 600000
        if num_pasajero>=151 and num_pasajero<=200:
            comision = 0.09 * 600000 * num_viajes + num_viajes * 600000
        if num_pasajero>200:
            comision = (0.09 * 600000* num_viajes + num_viajes * 600000) + (num_pasajero-200) * 60
        return comision

    if ruta==3:
        if num_pasajero<50:
            comision = 0
        if num_pasajero>=50 and num_pasajero<=100:
            comision = 0.10 * 800000
        if num_pasajero>=101 and num_pasajero<=150:
            comision = 0.13 * 800000
        if num_pasajero>=151 and num_pasajero<=200:
            comision = 0.15 * 800000
        if num_pasajero>200:
            comision = 0.15 * 800000 + (num_pasajero-200) * 100
        return comision

    if ruta==4:
        if num_pasajero<50:
            comision = 0
        if num_pasajero>=50 and num_pasajero<=100:
            comision = 0.125 * 1000000
        if num_pasajero>=101 and num_pasajero<=150:
            comision = 0.15 * 1000000
        if num_pasajero>=151 and num_pasajero<=200:
            comision = 0.17 * 1000000
        if num_pasajero>200:
            comision = 0.17 * 1000000 + (num_pasajero-200) * 150
        return comision 

def servicio_encomiedades(ruta, menos_10, entre_10_20, mas_20, peso, peso_menos_10, peso_entre_10_20, peso_mas_20):
    comision_50=0
    comision_50_100=0
    comision_101_130=0
    comision_130=0
    comision=0

    if ruta==1 or ruta==2:
        if menos_10<50:
            if peso_menos_10<10:
                comision_50 = 100 * menos_10
            if peso_menos_10>=10:
                comision_50 = 120 * menos_10
        
        comision = comision_50

        if entre_10_20<50:
            if peso_entre_10_20<10:
                comision_50 = 100 * entre_10_20
            if peso_entre_10_20>=10:
                comision_50 = 120 * entre_10_20
      
        comision = comision_50 + comision

        if mas_20<50:
            if peso_mas_20<10:
                comision_50 = 100 * mas_20
            if peso_mas_20>=10:
                comision_50 = 120 * mas_20

        comision = comision_50 + comision
 
        if menos_10>=50 and menos_10<=100:
            if peso_menos_10<10:
                comision_50_100 = 120 * menos_10
            if peso_menos_10>=10:
                peso_menos_10 = 140 * menos_10  

        comision = comision_50_100 + comision

        if entre_10_20>=50 and entre_10_20<=100:
            if peso_entre_10_20<10:
                comision_50_100 = 120 * entre_10_20
            if peso_entre_10_20>=10:
                comision_50_100 = 140 * entre_10_20  

        comision = comision_50_100 + comision

        if mas_20>=50 and mas_20<=100:
            if peso_mas_20<10:
                comision_50_100 = 120 * mas_20
            if peso_mas_20>=10:
                comision_50_100 = 140 * mas_20       

        comision = comision_50_100 + comision

        if menos_10>=101 and menos_10<=130:
            if peso_menos_10<10:
                comision_101_130 = 150 * menos_10
            if peso_menos_10>=10:
                comision_101_130 = 160 * menos_10  

        comision = comision_101_130 + comision  

        if entre_10_20>=101 and entre_10_20<=130:
            if peso_entre_10_20<10:
                comision_101_130 = 150 * entre_10_20
            if peso_entre_10_20>=10:
                comision_101_130 = 160 * entre_10_20   

        comision = comision_101_130 + comision  

        if mas_20>=101 and mas_20<=130:
            if peso_mas_20<10:
                comision_101_130 = 150 * mas_20
            if peso_mas_20>=10:
                comision_101_130 = 160 * mas_20    

        comision = comision_101_130 + comision  

        if menos_10>130:
            if peso_menos_10<10:
                comision_130 = 160 * menos_10
            if peso_menos_10>=10:
                comision_130 = 180 * menos_10   

        comision = comision_130 + comision  

        if entre_10_20>130:
            if peso_entre_10_20<10:
                comision_130 = 160 * entre_10_20
            if peso_entre_10_20>=10:
                comision_130 = 180 * entre_10_20  

        comision = comision_130 + comision  

        if mas_20>130:
            if peso_mas_20<10:
                comision_130 = 160 * mas_20
            if peso_mas_20>=10:
                comision_130 = 180 * mas_20      

        comision = comision_130 + comision  

        return comision

    if ruta==3 or ruta==4:
        if menos_10<50:
            if peso_menos_10<10:
                comision_50 = 130 * menos_10
            if peso_menos_10>=10 and peso_menos_10<=20:
                comision_50 = 140 * menos_10
            if peso_menos_10>20:
                comision_50 = 170 * menos_10
        
        comision = comision_50

        if entre_10_20<50:
            if peso_entre_10_20<10:
                comision_50 = 130 * entre_10_20
            if peso_entre_10_20>=10 and peso_entre_10_20<=20:
                comision_50 = 140 * entre_10_20
            if peso_entre_10_20>20:
                comision_50 = 170 * entre_10_20

        comision = comision_50 + comision

        if mas_20<50:
            if peso_mas_20<10:
                comision_50 = 130 * mas_20
            if peso_mas_20>=10 and peso_mas_20<=20:
                comision_50 = 140 * mas_20
            if peso_mas_20>20:
                comision_50 = 170 * mas_20

        comision = comision_50 + comision

        if menos_10>=50 and menos_10<=100:
            if peso_menos_10<10:
                comision_50_100 = 160 * menos_10
            if peso_menos_10>=10 and peso_menos_10<=20:
                comision_50_100 = 180 * menos_10
            if peso_menos_10>20:
                comision_50_100 = 210 * menos_10 

        comision = comision_50_100 + comision 

        if entre_10_20>=50 and entre_10_20<=100:
            if peso_entre_10_20<10:
                comision_50_100 = 160 * entre_10_20
            if peso_entre_10_20>=10 and peso_entre_10_20<=20:
                comision_50_100 = 180 * entre_10_20
            if peso_entre_10_20>20:
                comision_50_100 = 210 * entre_10_20 

        comision = comision_50_100 + comision

        if mas_20>=50 and mas_20<=100:
            if peso_mas_20<10:
                comision_50_100 = 160 * mas_20
            if peso_mas_20>=10 and peso_mas_20<=20:
                comision_50_100 = 180 * mas_20
            if peso_mas_20>20:
                comision_50_100 = 210 * mas_20   

        comision = comision_50_100 + comision

        if menos_10>=101 and menos_10<=130:
            if peso_menos_10<10:
                comision_101_130 = 175 * menos_10
            if peso_menos_10>=10 and peso_mas_20<=20:
                comision_101_130 = 200 * menos_10
            if peso_menos_10>20:
                comision_101_130 = 250 * menos_10   

        comision = comision_101_130 + comision

        if entre_10_20>=101 and entre_10_20<=130:
            if peso_entre_10_20<10:
                comision_101_130 = 175 * entre_10_20
            if peso_entre_10_20>=10 and peso_entre_10_20<=20:
                comision_101_130 = 200 * entre_10_20
            if peso_entre_10_20>20:
                comision_101_130 = 250 * entre_10_20   

        comision = comision_101_130 + comision  

        if mas_20>=101 and mas_20<=130:
            if peso_mas_20<10:
                comision_101_130 = 175 * mas_20
            if peso_mas_20>=10 and peso_mas_20<=20:
                comision_101_130 = 200 * mas_20
            if peso_mas_20>20:
                comision_101_130 = 250 * mas_20     

        comision = comision_101_130 + comision

        if menos_10>130:
            if peso_menos_10<10:
                comision_130 = 200 * menos_10
            if peso_menos_10>=10 and peso_menos_10<=20:
                comision_130 = 250 * menos_10
            if peso_menos_10>20:
                comision_130 = 300* menos_10  
        
        comision = comision_130 + comision

        if entre_10_20>130:
            if peso_entre_10_20<10:
                comision_130 = 200 * entre_10_20
            if peso_entre_10_20>=10 and peso_entre_10_20<=20:
                comision_130 = 250 * entre_10_20
            if peso_entre_10_20>20:
                comision_130 = 300* entre_10_20   

        comision = comision_130 + comision  

        if mas_20>130:
            if peso_mas_20<10:
                comision_130 = 200 * mas_20
            if peso_mas_20>=10 and peso_mas_20<=20:
                comision_130 = 250 * mas_20
            if peso_mas_20>20:
                comision_130 = 300* mas_20     
        
        comision = comision_130 + comision

        return comision_50+comision_50_100+comision_101_130+comision_130

def gastos_ayudante_seguro(comision_total):
    if comision_total<1000000:
        ayudante = comision_total * 0.05
        seguro = comision_total * 0.03
    if comision_total>=1000000 and comision_total<=2000000:
        ayudante = comision_total * 0.08
        seguro = comision_total * 0.04
    if comision_total>=2000001 and comision_total<=4000000:
        ayudante = comision_total * 0.10
        seguro = comision_total * 0.06
    if comision_total>4000000:
        ayudante = comision_total * 0.13
        seguro = comision_total * 0.09

    return ayudante, seguro

def subsidio_gasolina(peso, ruta, num_pasajero, peso_total, precio_galon):
    if ruta==1:
        if peso_total<5000:
            subsidios=(precio_galon)*150
        if peso_total>=5000 and peso_total<=10000:
            aux=(precio_galon)*150
            subsidios=aux+aux*0.10
        if peso_total>10000:
            aux=(precio_galon)*150
            subsidios=aux+aux*0.25
        
        return subsidios

    if ruta==2:
        if peso_total<5000:
            subsidios=(precio_galon)*167
        if peso_total>=5000 and peso_total<=10000:
            aux=(precio_galon)*167
            subsidios=aux+aux*0.10
        if peso_total>10000:
            aux=(precio_galon)*167
            subsidios=aux+aux*0.25

        return subsidios

    if ruta==3:
        if peso_total<5000:
            subsidios=(precio_galon)*184
        if peso_total>=5000 and peso_total<=10000:
            aux=(precio_galon)*184
            subsidios=aux+aux*0.10
        if peso_total>10000:
            aux=(precio_galon)*184
            subsidios=aux+aux*0.25

        return subsidios

    if ruta==4:
        if peso_total<5000:
            subsidios=(precio_galon)*203
        if peso_total>=5000 and peso_total<=10000:
            aux=(precio_galon)*203
            subsidios=aux+aux*0.10
        if peso_total>10000:
            aux=(precio_galon)*203
            subsidios=aux+aux*0.25

        return subsidios

def serie(number):
    lista = list(range(1,number+1))
    total = 0
    for i in range(1,number+1):
        total = i+total
    promedio = total/number
    return lista, total, promedio

def sumatoria(number):
    lista = list(range(1,number+1))
    total = 1
    for i in range(1,number+1):
        total = i*total
    return total
    