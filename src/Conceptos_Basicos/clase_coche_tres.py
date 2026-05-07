class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            return f"{self.marca} {self.modelo} encendido"

        return f"{self.marca} {self.modelo} ya estaba encendido"

    def apagar(self):
        if self.encendido:
            self.encendido = False
            self.velocidad = 0
            return f"{self.marca} {self.modelo} apagado"

        return f"{self.marca} {self.modelo} ya estaba apagado"
    
mi_coche = Coche("Toyota", "Corolla")

print(mi_coche.encender())
print(mi_coche.encender())
print(mi_coche.apagar())