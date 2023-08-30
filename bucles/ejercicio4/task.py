# format(variable, ".2f"),
ct = float(input("¿Cantidad a invertir?"))
intrs = float(input("¿Interés porcentual anual?"))
ans=int(input("¿Años?"))
for i in range(1, ans+1):
    cp=ct*(1+intrs/100)**i
    print(f"Capital tras {i} años: {round(cp, 2)}")