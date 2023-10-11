"""import agregar_contacto
from buscar_contacto import buscar_contacto"""


def agregar_un_contacto(agenda, nombre, telefono):
    """
    Usar el módulo agregar_contacto
    """
    agenda[nombre] = telefono

def buscar_un_contacto(agenda, nombre):
    """
    Usar el módulo buscar_contacto
    """
    nombre=input("Escriba el nombre del contacto a buscar")
    if nombre in agenda:
        print(nombre, agenda.get(nombre))

def ver_contactos(agenda):
    print(agenda)

def mostrar_menu():
    print("Menú de opciones:")
    print("(1) Agregar contacto")
    print("(2) Buscar contacto")
    print("(3) Ver contacto")
    print("(4) Salir")

def main():
    """
        Use el diccionario vacio agenda = {} para agregar, eliminar o ver las tareas
    """
    agenda = {}
    opcion = ""
    while opcion != "4":
        mostrar_menu()
        opcion = input("Escoja una opción: ")
        if opcion == "1":
            a=input("Agrega el nuevo contacto: ")
            b=input(a+":")
            agregar_un_contacto(agenda, a, b)
        elif opcion == "2":
            a = input("Buscar la agenda: ").title()
            buscar_un_contacto(agenda, a)
        elif opcion == "3":
            print(ver_contactos(agenda))
        elif opcion == "4":
            quit()


# TODO

if __name__ == "__main__":
    main()
