class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

# Creamos productos con y sin especificar el stock
laptop = Producto("Laptop XPS", 1200)
teclado = Producto("Teclado mecánico", 80, 15)

print(laptop.stock)
print(teclado.stock)