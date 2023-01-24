# Escribe una función calificaPalabras(diccionario) que reciba un diccionario con las 
# asignaturas y las notas numéricas de un alumno y devuelva otro diccionario con las asignaturas en 
# mayúsculas y las calificaciones correspondientes a las notas con palabras.  
# 
# El criterio será el siguiente:  nota <5 → Suspenso;  5 <= nota < 7 → Aprobado;   
# 7 <= nota < 9 → Notable; 9 <= nota <=10 → Sobresaliente. La nota no puede sobrepasar 10. 
# 
# Por ejemplo, la función recibe el diccionario {'Android':8.2, 'Hilos':5, 'Python':9.3, 'Interfaces':4.4} 
# y devuelve el diccionario {'ANDROID’:’Notable’,  ‘HILOS’:’Aprobado’, ‘PYTHON’:’Sobresaliente’, 
# ‘INTERFACES’:’Suspenso’ } 

from inputValidation import validarFloat, validarEntero

def calificaPalabras(diccionario):
	diccionario_nuevo = {}
	for clave, valor in diccionario.items():
		if valor < 5:
			diccionario_nuevo[clave.upper()] = "Suspenso"
		elif 5 <= valor < 7:
			diccionario_nuevo[clave.upper()] = "Aprobado"
		elif 7 <= valor < 9:
			diccionario_nuevo[clave.upper()] = "Notable"
		elif 9 <= valor <= 10:
			diccionario_nuevo[clave.upper()] = "Sobresaliente"
	return diccionario_nuevo

def rellernarDiccionario(validarFloat, n):
	diccionario = {}
	for i in range(n):
		clave = input("Introduce el nombre de la "+ str(i+1) + "ª asignatura: ")
		valor = validarFloat("Introduce la nota de la "+ str(i+1) + "ª asignatura: ")
		diccionario[clave] = valor
	return diccionario

n = validarEntero("Introduce el número de asignaturas: ", True)
dic = rellernarDiccionario(validarFloat, n)
print("Diccionario original: ", dic)
print(calificaPalabras(dic))
