# TODO lista = input("Introduce los elementos de la lista separados por comas: ").split(",")
# diccionario = {lista[i]: i+1 for i in range(len(lista))}
# print(diccionario)
info={}
seguir= True
while seguir:
    dato=input("¿Qué dato quieres introducir?")
    respuesta=input(dato + ": ")
    info[dato]=respuesta
    print(info)
    seguir=input("¿Quieres añadir más información (Si/No)?")
    if seguir == "Si"or seguir== "si":
        seguir=True
    else:
        seguir= False