# Crea una función llamada histograma(lista_números) a la que se le pasa una lista de números 
# enteros. Se mostrará un histograma cuyas columnas midan el valor de los números.  
# Por ejemplo: histograma([4, 9, 2,7]) debería imprimir lo siguiente: 
# **** 
# ********* 
# ** 
# *******

from inputValidation import validarEntero

def histograma(lista_numeros) -> None:
	for numero in lista_numeros:
		print("*" * numero)
  
n = validarEntero("¿Cuántos números quieres introducir en la lista?: ", True)

lista = []
for i in range(n):
	numero =validarEntero("Introduce un número: ", True)
	lista.append(numero)

print("Histograma de la lista: ", lista)
print(histograma(lista))
