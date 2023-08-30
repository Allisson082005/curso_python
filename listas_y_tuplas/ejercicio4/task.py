numeros = []
for i in range(3):
    numero = int(input("Introduce un número ganador:"))
    numeros.append(numero)
    numeros.sort()
print("Los números ganadores son", numeros)