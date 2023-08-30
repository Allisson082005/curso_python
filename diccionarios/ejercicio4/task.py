meses = {
    1: "enero",
    2: "febrero",
    3: "marzo",
    4: "abril",
    5: "mayo",
    6: "junio",
    7: "julio",
    8: "agosto",
    9: "septiembre",
    10: "octubre",
    11: "noviembre",
    12: "diciembre"
}
fecha = input("Introduce una fecha en formato dd/mm/aaaa:")
dia, mes, anio = fecha.split("/")
fecha_formateada = "{} de {} de {}".format(dia, meses[int(mes)], anio)
print(fecha_formateada)