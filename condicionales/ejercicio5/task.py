edad=int(input("¿Cuál es tu edad?"))
inm=float(input("¿Cuales son tus ingresos mensuales?"))
if edad > 16 and inm >= 1000 :
    print("Tienes que cotizar")
else:
    print("No tienes que cotizar")