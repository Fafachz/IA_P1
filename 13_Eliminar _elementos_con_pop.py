#Elimina de la siguiente lista los elementos 'azul' y 'blanco'. Solo puedes eliminarlos utilizando el método pop().
#Además, tendrás que guardar esos dos colores en una nueva lista

#Crea lista de colores:
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

#Eliminamos color con por y lo almacenamos en un nuevo string
colazul = colores.pop(1)
colblan = colores.pop(7)

#Creamos nueva lista con los colores eliminados y almacenados
colguardados = [colazul, colblan]

#Imprimimos ambas listas para demostrar funcionamiento
print(colores)
print(colguardados)