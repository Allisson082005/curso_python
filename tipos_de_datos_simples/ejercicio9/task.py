
CI=float(input("¿Cantidad a invertir?"))
Ipa=float(input("¿Interés porcentual anual?"))
añs=int(input("¿Años?"))
resultado= CI*(1+Ipa/100)**añs
print("Capital final:", round(resultado, 2))