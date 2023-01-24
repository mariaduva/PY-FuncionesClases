# Escribe una función palabrasLongitud(frase) que reciba una frase y devuelva un diccionario 
# con las palabras que contiene y su longitud.  
# Por ejemplo, la función recibe la frase ‘Hola y adiós’ y devuelve un diccionario de la forma 
# {‘Hola’:4, ‘y’:1, ‘adiós’:5} 

def palabrasLongitud(frase):
	diccionario = {}
	for palabra in frase.split():
		diccionario[palabra] = len(palabra)
	return diccionario

frase = ""

while frase == "":
	frase = input("Introduce una frase: ")
	if frase == "":
		print("No has introducido ninguna frase.")

print(palabrasLongitud(frase))