nom=input("¿Cómo te llamas?")
s=input("¿Cuál es tu sexo (M o H)?")
if (s == "M" and nom.lower() < "m") or (s == "H" and nom.lower() > "n"):
    print("Tu grupo es A")
else:
    print("Tu grupo es B")
