def mostrar_menu():
    print("(1) Agregar tarea")
    print("(2) Eliminar tarea")
    print("(3) Ver tarea")
    print("(4) Salir")


def agregar_tarea(tareas, tarea):
    tareas.append(tarea)
    print("Tarea agregada: ", tarea)


def eliminar_tarea(tareas, indice):
    if 0<= indice < len(tareas)
        tarea_eliminada = tareas.pop(indice)
        print("Tarea eliminada: ", tarea_eliminada)
    else:
        print("Indice invalido, no se puede eliminar tarea.")



def ver_tareas(tareas):
    print("Tareas en la lista: ")
    for i
    tareas

def main():
    tareas = []
    opcion=""
    while opcion != "4":
        mostrar_menu()
        opcion = input("EScoja una opción: ")
        if opcion == "1":
            a = input("Añade una tarea: ")
            agregar_tarea(tareas, a)
        elif opcion == "2":
            
            a = input("Elimina una tarea: ")
            eliminar_tarea(tareas, a)
        elif opcion == "3":
            print(ver_tareas())
        elif opcion == "4":
            print("")
    """
    
        Use la lista vacia tareas = [] para agregar, eliminar o ver las tareas
    """

# TODO


if __name__ == "__main__":
    main()
