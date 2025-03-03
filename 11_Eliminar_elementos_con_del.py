#De esta lista, elimina los colores 'azul', 'marrón', 'negro' y 'rosa'. 
# Debes utilizar al menos una vez las posiciones negativas para eliminar un color. 
# Después, imprime la lista para ver los colores que se han eliminado.

#Creamos una lista
col = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
#Eliminamos los colores solicitados
del col[1]
del col[3]
del col[4]
del col[-3]
#Imprimimos los que quedan
print(col)