#Itera el diccionario teclado1 con un solo bucle for que muestre esto en la consola:

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

for x in teclado1:
	print(x,'=', teclado1[x] + '.') #Se hace de esta forma para que puedan imprimirse tanto las claves como los valores
