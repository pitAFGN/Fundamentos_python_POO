class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.area = ancho * alto
        self.perimetro = 2 * (ancho + alto)

# Creamos un rectángulo
rect = Rectangulo(5, 3)
print(rect.area)
print(rect.perimetro)