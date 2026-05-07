class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self._titular = titular
        self._saldo = saldo
        saldo = 0

    @property
    def titular (self):
        return self._titular

    @property
    def saldo (self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldoNuevo):
        if saldoNuevo < 0:
            raise ValueError("El saldo no puede ser negativo")
        else:
            self._saldo = saldoNuevo
            
    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo = self._saldo + cantidad
            return True
        else:
            return False
        
    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self._saldo:
            self._saldo = self._saldo - cantidad
            return True
        else:
            return False
    
def main():
    cuenta = CuentaBancaria("Juan", 1000)

    print(cuenta.titular)
    print(cuenta.saldo)

    cuenta.depositar(500)
    print(cuenta.saldo)

    cuenta.retirar(300)
    print(cuenta.saldo)

    print(cuenta.retirar(5000))

if __name__ == "__main__":
    main()