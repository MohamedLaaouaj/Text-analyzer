#Descripción del proyecto: Crear un analizador de texto.
texto = input("Igresa el texto: ")
letras = []

#Poner todo en minúsiculas para no tener problemas:
texto = texto.lower()

#Inputs de las letras a analizar sobre el texto:
letras.append(input("Ingresa la primer palabra: ").lower())
letras.append(input("Ingresa la segunda palabra: ").lower())
letras.append(input("Ingresa la tercera palabra: ").lower())

#Conocer la cantidad de letras del texto
print("\n")
print("CANTIDAD DE LETRAS: ")
cantidad_letras_0 = texto.count(letras[0])
cantidad_letras_1 = texto.count(letras[1])
cantidad_letras_2 = texto.count(letras[2])
print(f"Hemos encontrado {cantidad_letras_0} de la palabra \"{letras[0]}\"")
print(f"Hemos encontrado {cantidad_letras_1} de la palabra \"{letras[1]}\"")
print(f"Hemos encontrado {cantidad_letras_2} de la palabra \"{letras[2]}\"")

#Cantidad de las palabras
print("\n")
print("CANTIDAD DE PALABRAS:")
palabras = texto.split() #al separarlo su type es "list"
print(f"Hay {len(palabras)} palabras en el texto. ")

#Letras de inicio y de fin
print("\n")
print("LETRAS DE INICIO Y FIN: ")
print(f"La letra inicial es: {texto[0]} y la letra final es: {texto[-1]}")

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



