#¿Cuántos argumentos se utilizan en cada una de estas llamadas?

#def colores(*args):
#	pass

#colores('rojo', 'azul', 'verde', 'amarillo')  4 arcumentos
#colores('lila', 'negro', 'rojo')              3 argumentos
#colores('rosa')                               1 argumento
#colores('marrón', 'naranja')                  2 argumentos


print('Ejercicio Colores:')
#Completa el siguiente fragmento de código:

def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')
colores('Morado','Naranja')
print('\n')


print('Ejercicio Suma:')
#Crea una función que realice la suma de cinco números utilizando solo *args.
#Debes imprimir el resultado en la consola. La suma no se realizará directamente sobre el print().

def OpSuma(*args):
	resulado = args[0] + args[1] + args[2] + args[3] + args[4]
	print('El resultado de la operacion es:', resulado)
	
OpSuma(45, 47, 16, 21, 23) #152