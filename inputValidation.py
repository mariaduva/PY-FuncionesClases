# Función para validar la entrada de un número entero positivo 
# donde str es el mensaje que se muestra al usuario y nat es un booleano que indica
# si el número debe ser natural o no (puede ser negativo)
def validarEntero(str, nat):
	goodinput = False
	while not goodinput:
		try:
			number = int(input(str))
			if number > 0 and nat == True or nat == False:
				goodinput = True
				return number
			else:
				if nat == True:
					print("El número debe ser mayor que 0. Inténtalo de nuevo:")
		except ValueError:
			print("El valor introducido no es un número. Inténtalo de nuevo:")
   

# Función para validar la entrada de un número de tipo float
def validarFloat(str):
	while True:
		try:
			numero = float(input(str))
			if numero > 10 or numero < 0:
				print("La nota no puede ser mayor que 10 o menor que 0.")
				continue
			return numero
		except ValueError:
			print("La nota debe ser un número.")
			continue