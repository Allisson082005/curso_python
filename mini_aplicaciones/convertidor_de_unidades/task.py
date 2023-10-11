def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def kilometros_a_millas(kilometros):
    return kilometros * 0.621371

def litros_a_galones(litros):
    return litros * 0.264172

def mostrar_menu():
    print("1. Celsius a Fahrenheit")
    print("2. Kilómetros a millas")
    print("3. Litros a galones")

def main():
    while True:
        mostrar_menu()
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            celsius = float(input("Ingrese los grados Celsius: "))
            fahrenheit = celsius_a_fahrenheit(celsius)
            print(f"{celsius} grados Celsius son equivalentes a {fahrenheit} grados Fahrenheit.")
        elif opcion == 2:
            kilometros = float(input("Ingrese los kilómetros: "))
            millas = kilometros_a_millas(kilometros)
            print(f"{kilometros} kilómetros son equivalentes a {millas} millas.")
        elif opcion == 3:
            litros = float(input("Ingrese los litros: "))
            galones = litros_a_galones(litros)
            print(f"{litros} litros son equivalentes a {galones} galones.")
        else:
            break

if __name__ == "__main__":
    main()
