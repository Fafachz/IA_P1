

#El valor inicial de la variable x será de 0.
x = 0

#La condición de salida del bucle será mayor o igual a 30
while x <= 30:
    x += 1 #El valor de incremento será 1
    print(x) #Imprime todos los numeros
    #La ejecución se deberá romper cuando x valga 15
    if x == 15:
        #Cuando se rompa la ejecución del bucle deberás mostrar un mensaje indicándolo
        print('Se rompio la cadena del bucle cuando x valia:',x)
        break
    #Debes saltarte las ejecuciones con valor de x en 4, 6 y 10
    if x == 4 or x == 6 or x == 10:
        #En cada salto de ejecución, deberás mostrar los valores saltado con este mensaje
        print('Se saltó el valor ' ,x, ' de x')
        continue