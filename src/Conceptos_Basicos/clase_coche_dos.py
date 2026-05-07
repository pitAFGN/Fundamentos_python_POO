class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.kilometraje = 0

mi_coche = Coche("Toyota", "Corolla", "Azul")

print(f"Color inicial: {mi_coche.color}")
print(f"Kilometraje inicial: {mi_coche.kilometraje}")

mi_coche.color = "Rojo"
mi_coche.kilometraje = 1500

print(f"Nuevo color: {mi_coche.color}")
print(f"Kilometraje actual: {mi_coche.kilometraje}")