def monitoreo(codigo:str, sensores:tuple):
  result_final = {}
  data = [{'codigo': '010010','nom': 'Juan Pérez','dir': 'cr 30 25 80','zona': 1, 'sensores': 7},
          {'codigo': '020008','nom': 'Carolina Charris','dir': 'cr 84 70 27 Bod 4','zona': 2,'sensores': 5},
          {'codigo': '030011','nom': 'Juan Pérez','dir': 'cr 30 10 80','zona': 3,'sensores': 5},
          {'codigo': '020114','nom': 'Omar Acosta','dir': 'cr 30 25 80','zona': 2,'sensores': 5},
          {'codigo': '020115','nom': 'Camilo Fernández','dir': 'cr 30 25 80','zona': 2,'sensores': 5},
          {'codigo': '010020','nom': 'Juan Díaz','dir': 'cr 30 15 80','zona': 1,'sensores': 8}]
  resultado = []
  for i in data:
    for j in i.values():
      if j==codigo:
        result_1 = codigo
        result_2 = i['dir']
        zona = i['zona']
        if zona==1:
          result_3=3
        if zona==2 or zona==3:
          result_3=2
        sensoresT = i['sensores']

  count = 0
  for x in sensores:
    if x =='1':
      count = count +1
  if count==sensoresT:
    result_5='correcto'
  else:
    result_5='revisar'
    

  result_3 = str(result_3)+' guardias'
  result_4 = count
  if count ==0:
    result_final = [{}]
  else:
    result_final = {'codigo_cliente': result_1, 'direccion': result_2, 'cantidad_guardias': result_3, 'sensores_activos': result_4, 'estado_sensores': result_5}
  return result_final

codigo = input('Ingrese el codigo: ')
print('\n')
num=int(input("Ingrese el número de sensores: "))
print('\n')
sensores=[]
for i in range(num):
	sensores.append(input("Ingrese 0 ó 1 para el Sensor #{} : ".format(i+1)))
print('\n')
print(monitoreo(codigo, sensores))