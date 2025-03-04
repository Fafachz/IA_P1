#Haz una tupla que contenga cuatro colores de tu elección. 
#Tendrás que poner una condición con el condicional if para cada color que le avise al usuario que el color 
#está en la tupla con un mensaje como este: print('El color rojo está admitido') y una condición False para
#contemplar cualquier color que no esté en la tupla con un mensaje como este: print('Color no admitido'). 
#No puedes utilizar el operador ==. 
#Además tendrás que hacer esto con un input() que permita introducir un color al usuario.

buscar = input('Introduce el color a bucas:\n')
colors = ('azul', 'amarillo', 'morado', 'rojo', 'naranja','negro', 'verde')

if buscar in colors[0]:
	print('El azul está en la lista.')
elif buscar in  colors[1]:
	print('El color amarillo esta en la lista')
elif buscar in  colors[2]:
	print('El color morado esta en la lista')
elif buscar in  colors[3]:
	print('El color rojo esta en la lista')
elif buscar in  colors[4]:
	print('El color naranja esta en la lista')
elif buscar in  colors[5]:
	print('El color negro esta en la lista')
elif buscar in  colors[6]:
	print('El color verde esta en la lista')
else:
	print('El color que buscas no está en la lista.')
