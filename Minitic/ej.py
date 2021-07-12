def estado_nivel():
  codigo_nivel={}
  print("Ingrese el número de tanques:" , end=" ")
  total_tanques = int(input())
  id = 'TA'
  sensores={}
  aux={}
  print("Hay líquido en nivel alto ingrese (1), No hay líquido en nivel alto {0}: ")
  for i in range(total_tanques):
    lista=[]
    identificador = id + '00' + str(i+1)
    print('\n')
    for j in range(3):
      num_sensor = str(j+1)
      sensor='sensor'+num_sensor
      estado=int(input("Para el tanque {} ingrese el nivel para el sensor {}: ".format(identificador, num_sensor)))
      if estado==1:
        estado=True
      if estado==0:
        estado=False
      lista.append(estado)

    if lista[0]==False and lista[1]==False and lista[2]==False:
      nivel='Vacío'
    elif lista[0]==True and lista[1]==False and lista[2]==False:
      nivel='Nivel bajo'
    elif lista[0]==True and lista[1]==True and lista[2]==False:
      nivel='Nivel medio'
    elif lista[0]==True and lista[1]==True and lista[2]==True:
      nivel='Nivel alto'
    else:
      print('Revisar sensores')
      nivel='Revisar sensores'

    codigo_nivel[identificador]=nivel
  return codigo_nivel

codigo_nivel = estado_nivel()

print('\n********************************')
print(codigo_nivel)

print('\n********************************')
for key in codigo_nivel:
  print(key, ":", codigo_nivel[key])