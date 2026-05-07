class Fecha:
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año

    @classmethod
    def desde_texto(cls, texto):
        dia, mes, año = map(int, texto.split('-'))
        return cls(dia, mes, año)

    @classmethod
    def hoy(cls):
        import datetime
        fecha_actual = datetime.date.today()
        return cls(fecha_actual.day, fecha_actual.month, fecha_actual.year)

fecha1 = Fecha(15, 3, 2023)
fecha2 = Fecha.desde_texto("25-12-2023")
fecha3 = Fecha.hoy()

print(f"{fecha1.dia}/{fecha1.mes}/{fecha1.año}")
print(f"{fecha2.dia}/{fecha2.mes}/{fecha2.año}")