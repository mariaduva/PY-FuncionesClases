# Escribe una clase llamada Poligono() que genera objetos de polígono de 3 o más lados.  
# Al crear un objeto, en el constructor __init__ ( ), se indica el número de lados que va a tener y 
# se crea una lista que va a tener ese número de elementos cuyos valores iniciales serán 0. 

#La clase Poligono() tendrá un método llamado darlados( ) que le pedirá al usuario que 
# introduzca uno a uno los valores de todos los lados. 

# • La clase Polígono() tendrá otro método llamado verlados( ) que mostrará uno a uno los 
# valores introducidos de todos los lados. 
# • Se va a crear una clase llamada Triangulo() que hereda de la clase  Poligono().  
# Al crear un objeto triangulo, se invoca al constructor de la clase Poligono() al que se indica el 
# número de lados = 3. 
# • La clase Triangulo() tendrá un método area( ) que calcule y muestre el área del triángulo. 
# Puede ser cualquier tipo de triángulo. Puedes usar la fórmula de Herón. 
# • La clase Triangulo() tendrá un método perimetro( ) que calcule y muestre el perímetro del 
# triángulo (suma de sus lados). 
# • Crea dos objetos de la clase Triangulo() y muestra el resultado de ejecutar todos los 
# métodos tanto de la clase Polígono() como de la clase Triangulo(). 

from inputValidation import validarEntero

class Poligono:
	def __init__(self, lados):
		self.lados = lados
		self.lista_lados = [0] * lados

	def darlados(self):
		for i in range(self.lados):
			self.lista_lados[i] = validarEntero("Introduce el lado " + str(i+1) + ": ", True)

	def verlados(self):
		for i in range(self.lados):
			print("Lado " + str(i+1) + ": " + str(self.lista_lados[i]))
   
   
class Triangulo(Poligono):
	def __init__(self):
		super().__init__(3)

	def area(self):
		a = self.lista_lados[0]
		b = self.lista_lados[1]
		c = self.lista_lados[2]
		s = (a + b + c) / 2
		area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
		print("El área del triángulo es: " + str(area))

	def perimetro(self):
		perimetro = self.lista_lados[0] + self.lista_lados[1] + self.lista_lados[2]
		print("El perímetro del triángulo es: " + str(perimetro))

ans = input("¿Vas a introducir algún triángulo? (S/N)")
if ans == "S" or ans == "s":
	triangulos = [None] * validarEntero("Introduce el número de triángulos: ", True)
	for i in range(len(triangulos)):
		print("Triángulo " + str(i+1) + ": ")
		triangulos[i] = Triangulo()
		triangulos[i].darlados()
		triangulos[i].verlados()
		triangulos[i].area()
		triangulos[i].perimetro()

ans = input("¿Vas a introducir alguna figura? (S/N)")
if ans == "S" or ans == "s":
        figuras = [None] * validarEntero("Introduce el número de figuras: ", True)
        for i in range(len(figuras)):
            print("Polígono " + str(i+1) + ": ")
            figuras[i] = Poligono(validarEntero("Introduce el número de lados del polígono " + str(i+1) + ": ", True))
            figuras[i].darlados()
            figuras[i].verlados()

