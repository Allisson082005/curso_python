productos={"Plátano": 50, "Manzana": 60, "Pera": 70, "Naranja": 80}
fruta=input("¿Qué fruta quieres?").title()
precio=float(input("¿Cuántos kilos?"))
if fruta in productos:
    print(precio, "kilos de", fruta , "valen", productos[fruta]*precio, "colones")
else:
    print("Lo siento, la fruta", fruta, "no está disponible.")