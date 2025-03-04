#Añade a la siguiente lista los colores 'magenta' y 'turquesa' utilizando insert(). 
#Tendrás que posicionar 'magenta' en la posición siguiente a la de 'lila' y 'turquesa' en la penúltima posición. 
#Deberás hacer esto utilizando posiciones de lista negativas.

#Creamos y imprimimos una lista de colores:
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print(colores)

#Agregamos dos colores utilizando insert() y e imprimimos con print()
colores.insert(-4, 'magenta'), colores.insert(-1,'turquesa')
print(colores)