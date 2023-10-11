def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

def mostrar_menu():
    print("Menú de opciones:")
    print("(1) Suma")
    print("(2) Resta")
    print("(3) Multiplicación")
    print("(4) División")
    print("(5) Salir")

def main(menu=None):
    mostrar_menu()
   opcion = input("Seleccione una opción: ")
   a=int(input("Inserte el primer número: "))
   b=int(input("Inserte el segundo número: "))
    while opcion != mn[5]:
        if opcion == "1" :
           print("resultados", suma(a,b))
        elif opcion == "2":
            print("resultados", resta(a, b))
        elif opcion == "3":
            print("resultados", multiplicacion(a, b))
        elif opcion == "4":
            print("resultados", division(a, b))
        elif opcion == "5":
            print("")



if __name__ == "__main__":
    main()
