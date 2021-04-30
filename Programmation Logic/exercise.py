def switch():
    if nGeneral == 1:
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

    elif nGeneral == 2:
        #region exercise 2
        #2. Build a program that asks for 3 numbers on the screen and then say which is the largest of the numbers entered?
        print("Ingrese tres numeros:")
        num1=int(input())
        num2=int(input())
        num3=int(input())

        from module import bigger_number
        print("El mayor de los tres números es {0}".format(bigger_number(num1,num2,num3)))
        #endregion

    elif nGeneral == 3:
        #region exercise 3
        #3. Build a program that asks for 3 numbers on the screen and then says phones is the largest, the middle one and the smallest of the entered numbers
        print("Ingrese tres numeros:")
        num1=int(input())
        num2=int(input())
        num3=int(input())

        from module import order
        print("{0}".format(order(num1,num2,num3)))
        #endregion

    elif nGeneral == 4:
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
        
    elif nGeneral == 5:
        #region exercise 5
        #5. Build a program that asks for a year and then determine if the year is leap or not.
        print("Ingrese el año: ")
        num=int(input())

        from module import year_leap
        print(year_leap(num))
        #endregion

    elif nGeneral == 6:
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

    elif nGeneral == 7:
        #region exercise 7
        #7. A desktop store makes the following discounts: if the customer purchases less than 5 units, a 10% discount on the purchase is granted; if the number of units is greater than or equal to five but less than 10, 20% and, if there are 10 or more, it is given 40%.

        print("Número de escritorios: ")
        units=int(input())

        from module import discount
        print(discount(units))
        #endregion
   
    elif nGeneral == 8:
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

    elif nGeneral == 9:
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
    
    elif nGeneral == 10:
        #region exercise 10
        #View pdf
        print("Costo de compra ($)....................................................:", end=" ")
        CC=int(input())
        print("Tipo de producto [P]erecedero, [N]o perecedero.........................:", end=" ")
        TP=input()
        print("Tipo de conservación [F]rio, [A]mbiente................................:", end=" ")
        TC=input()
        print("Periodo de conservación (días).........................................:", end=" ")
        PC=int(input())
        print("Periodo de almacenamiento (días).......................................:", end=" ")
        PA=int(input())
        print("Volumen (litros).......................................................:", end=" ")
        VOL=int(input())
        print("Medio de almacenamiento [N]evera, [C]ongelador, [E]estanteria, [G]uacal:", end=" ")
        MA=input()
        from module import almacenes_suceso
        result = almacenes_suceso(CC, TP, TC, PC, PA, VOL, MA)

        print("\n")
        print("Costos de almacenamiento..............................................: {0}".format(result[0]))
        print("Porcentaja de depreciación............................................: {0}".format(result[1]))
        print("Costo de exhibición...................................................: {0}".format(result[2]))
        print("Valor producto........................................................: {0}".format(result[3]))
        print("Valor venta...........................................................: {0}".format(result[4]))
        #endregion

    elif nGeneral == 11:
        #region exercise 11
        #view pdf
        print("Ruta [1][2][3][4]...............................:", end=" ")
        ruta=int(input())
        print("Número de viajes................................:", end=" ")
        num_viajes=int(input())
        print("Número de pasajeros total.......................:", end=" ")
        num_pasajero=int(input())
        print("Número de encomiendas de menos de 10Kg..........:", end=" ")
        menos_10=int(input())
        print("Número de encomiendas entre 10Kg y menos de 20Kg:", end=" ")
        entre_10_20=int(input())
        print("Número de encomiendas de más de 20Kg............:", end=" ")
        mas_20=int(input())

        peso_menos_10 = menos_10*10
        peso_entre_10_20 = entre_10_20*15
        peso_mas_20 = mas_20*20
        peso = menos_10*10 + entre_10_20*15+ mas_20*20


        peso_total=peso+num_pasajero*60
        precio_galon=8860/39

        from module import comision_pasajero
        from module import servicio_encomiedades
        from module import gastos_ayudante_seguro
        from module import subsidio_gasolina

        comision1 = (comision_pasajero(num_pasajero, ruta, num_viajes))
        print("Ingresos por Pasajeros.........................: {0}".format(comision1))

        comision2 = (servicio_encomiedades(ruta, menos_10, entre_10_20, mas_20, peso, peso_menos_10, peso_entre_10_20, peso_mas_20))
        print("Ingresos por Encomiendas.......................: {0}".format(comision2))

        comision_total=comision1+comision2
        print("TOTAL INGRESOS.................................: {0}".format(comision_total))

        seguro_ayudante = gastos_ayudante_seguro(comision_total)
        print("Pago Ayudante..................................: {0}".format(seguro_ayudante[0]))
        print(seguro_ayudante[1])

        total_subsidio = subsidio_gasolina(peso, ruta, num_pasajero, peso_total, precio_galon)
        print("Pago Combustible...............................: {0}".format(total_subsidio))

        total_deducciones = seguro_ayudante[0] + seguro_ayudante[1] + total_subsidio
        print("TOTAL DEDUCCIONES..............................: {0}".format(total_deducciones))

        print("TOTAL A LIQUIDAR...............................: {0}".format(comision_total-total_deducciones))
        #endregion

    elif nGeneral == 12:
        #region exercise 12
        #7. Build a program that prints the top N, their sum and their average.

        print("Cuantos números desea:", end=" ")
        number=int(input())

        from module import serie
        datos = serie(number)
        print(datos[0])
        print("La suma es: {0}".format(datos[1]))
        print("El promedio es: {0}".format(datos[2]))
        #endregion
   
    elif nGeneral == 13:
        #region exercise 12
        #7. Build a program that prints the top N, their sum and their average.

        print("Cuantos números desea:", end=" ")
        number=int(input())

        from module import sumatoria
        datos = sumatoria(number)
        print("El factorial es: {0}".format(datos))
        #endregion

    elif nGeneral == 14:
        #region exercise 12
        #7. Build a program that prints the top N, their sum and their average.

        print("Cuantos términos desea:", end=" ")
        number=int(input())

        print("Digita el valor de x:", end=" ")
        x=int(input())

        from module import taylor
        datos = taylor(number, x)
        print("El factorial es: {0}".format(datos))
        #endregion

    elif nGeneral == 0:
        print("Ingrese una opción correcta entre el ejercicio 1 al 37")
        sys.exit()
    
    elif nGeneral != range(1,37):
        print("Ingrese una opción correcta entre el ejercicio 1 al 37 ó el número cero para terminar!!!")

import sys

while True:
    try:
        print("\nIngrese un número de ejercicio entre 1 y 37: ")
        nGeneral = int(input())

    except ValueError:
        print("\nElección incorrecta, por favor ingrese un número valido ó el número cero para terminar!!!\n")

    else:
        switch()