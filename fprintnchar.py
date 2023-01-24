# Escribe una función generar_n_caracteres(n, carácter) a la que se le pasa un número 
# entero n y un carácter. Devolverá el carácter multiplicado por n.  
# Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx". Tantas x como indique el número. 

from inputValidation import validarEntero

def generar_n_caracteres(n, caracter):
	return caracter * n

n = validarEntero("Introduce un número: ", True)
char = input("Introduce un caracter: ")
print(generar_n_caracteres(n, char))