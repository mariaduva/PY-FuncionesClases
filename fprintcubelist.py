# Escribe una función funcionLista(función, lista) que reciba otra función creada 
# anteriormente y una lista, y devuelva otra lista con el resultado de aplicar la función dada a cada 
# uno de los elementos de la lista.  
# Por ejemplo, la función que se le pasa calcula el cubo de un número. 
# La lista que se pasa es una lista de números enteros. A cada número de la lista se le aplica la 
# función y se calculará el cubo de todos ellos, mostrándolos en otra lista nueva.  
# Si la lista que se pasara fuera [1,2,3,4,5] la función devolvería [1,8,27,64,125] 

from inputValidation import validarEntero

def funcionCubo(numero):
	return numero ** 3

def funcionLista(funcionCubo, lista):
	lista_nueva = []
	for numero in lista:
		lista_nueva.append(funcionCubo(numero))
	return lista_nueva

n = validarEntero("¿Cuántos números quieres introducir en la lista?: ", True)
print(n)

lista = []
for i in range(n):
	numero =validarEntero("Introduce un número: ", False)
	lista.append(numero)
 
print("Lista original: ", lista)
print("Lista con el cubo de cada elemento: ", funcionLista(funcionCubo, lista))
