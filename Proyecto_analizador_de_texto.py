#Descripción del proyecto: Crear un analizador de texto.
texto = input("Igresa el texto: ")
palabra = []

#Poner todo en minúsiculas para no tener problemas:
texto = texto.lower()

#Inputs de las palabras a analizar sobre el texto:
palabra.append(input("Ingresa la primer palabra: ").lower())
palabra.append(input("Ingresa la segunda palabra: ").lower())
palabra.append(input("Ingresa la tercera palabra: ").lower())

#Conocer la cantidad de palabras elegidas que se repiten.
print("\n")
print("CANTIDAD DE PALABRAS: ")
cantidad_palabra_0 = texto.count(palabra[0])
cantidad_palabra_1 = texto.count(palabra[1])
cantidad_palabra_2 = texto.count(palabra[2])
print(f"Hemos encontrado {cantidad_palabra_0} de la palabra \"{palabra[0]}\"")
print(f"Hemos encontrado {cantidad_palabra_1} de la palabra \"{palabra[1]}\"")
print(f"Hemos encontrado {cantidad_palabra_2} de la palabra \"{palabra[2]}\"")

#Cantidad de palabras totales
print("\n")
print("CANTIDAD DE PALABRAS:")
palabras = texto.split() #al separarlo su type es "list"
print(f"Hay {len(palabras)} palabras en el texto. ")

#Letras de inicio y de fin
print("\n")
print("LETRAS DE INICIO Y FIN: ")
print(f"La letra inicial es: {texto[0]} y la letra final del texto es: {texto[-1]}")

#Texto invertido
print("\n")
print("TEXTO INVERTIDO: ")
palabras.reverse()
texto_invertido = " ".join(palabras) #Join lo que hace es agregar lo que le indiques "fdsv" entre los elementos de la lista.
print(f"El texto invertido es: '{texto_invertido}'")

#Python se encuetra en el texto?
print("\n")
print("BUSCANDO LA PALABRA 'Python': ")
respuesta = "python" in texto
dic = {True:"sí", False:"no"}
print(f"La palabra 'python' se encuentra en el texto? {dic[respuesta]}")

#Mohamed_Laaouaj



