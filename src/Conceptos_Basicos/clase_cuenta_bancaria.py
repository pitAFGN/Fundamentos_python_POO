class CuentaBancaria:
    tasa_interes = 0.03

    def __init__(self, titular, saldo_inicial, pin):
        self.titular = titular
        self._saldo = saldo_inicial
        self.__pin = pin

    def verificar_pin(self, pin_ingresado):
        return self.__pin == pin_ingresado

cuenta = CuentaBancaria("Ana López", 1000, "1234")

print(cuenta.titular)
print(cuenta._saldo)
print(cuenta._CuentaBancaria__pin)