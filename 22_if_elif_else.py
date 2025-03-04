edad = int(input('¿Cuál es tu edad?\n'))
if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad >= 1 and edad < 18:
	print('Eres menor de edad.')
elif edad >= 18 and edad < 45:
	print('Eres mayor de edad.')
elif edad >=45 and edad < 100:
	print('Eres adulto mayor.')
elif edad >= 100 and edad <= 120:
	print('Eres un viejito')
else:
	print('Edad no válida.')