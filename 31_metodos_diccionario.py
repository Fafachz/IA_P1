#Elimina el diccionario teclado1 entero . De teclado2 elimina las claves 'Categoría' y 'Precio'.
#Muestra la última clave ('Modelo') que queda en la consola.

teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

del teclado1 #Eliminamos el diccionario completo
del teclado2['Categoría'] #Eliminamos clave categoría
del teclado2['Precio'] #Eliminamos clave precio
print(teclado2['Modelo']) #Mostramos ultima clave restante