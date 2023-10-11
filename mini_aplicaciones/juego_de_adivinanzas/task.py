import random

def generar_numero_aleatorio(minimo, maximo):
    return random.randint(minimo, maximo)

def mostrar_menu():
    print("1. Adivinar número")
    print("2. Salir")

def main():
    minimo = 1
    maximo = 100
    numero_aleatorio = generar_numero_aleatorio(minimo, maximo)
    opcion = 0

    while opcion != 2:
        mostrar_menu()
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            intentos = 0
            adivinado = False

            while not adivinado:
                intentos += 1
                numero_usuario = int(input("Ingrese un número entre {} y {}: ".format(minimo, maximo)))

                if numero_usuario < numero_aleatorio:
                    print("El número es demasiado bajo.")
                elif numero_usuario > numero_aleatorio:
                    print("El número es demasiado alto.")
                else:
                    print("¡Adivinaste el número en {} intentos!".format(intentos))
                    adivinado = True
        elif opcion == 2:
            print("¡Gracias por jugar!")
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
