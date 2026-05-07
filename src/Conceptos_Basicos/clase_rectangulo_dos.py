class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    @property
    def area(self):
        return self.ancho * self.alto

    @property
    def perimetro(self):
        return 2 * (self.ancho + self.alto)

rect = Rectangulo(5, 3)

print(f"Área: {rect.area}")
print(f"Perímetro: {rect.perimetro}")

rect.ancho = 7
print(f"Nueva área: {rect.area}")