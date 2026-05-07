class Producto:
    impuesto = 0.21

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

laptop = Producto("Laptop", 1000)

print(laptop.nombre)
print(laptop.precio)
print(laptop.impuesto)
print(Producto.impuesto)