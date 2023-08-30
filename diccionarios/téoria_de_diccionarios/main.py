if __name__ == "__main__":
    # Write your solution here
    pass
diccionario = {}
respuesta = input("Ingrese su respuesta: ")
diccionario["clave"] = respuesta
print(diccionario["clave"])

diccionario = {}
respuesta = input("Ingrese su respuesta: ")
diccionario["pregunta"] = respuesta

respuesta_input = input(diccionario["pregunta"])
diccionario[respuesta] = respuesta_input

print(diccionario[respuesta])
