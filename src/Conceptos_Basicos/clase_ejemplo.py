class Ejemplo:
    """Clase de ejemplo para mostrar atributos especiales"""
    def __init__(self, valor):
        self.valor = valor

obj = Ejemplo(42)

print(obj.__class__)
print(Ejemplo.__name__)
print(Ejemplo.__doc__)
print(obj.__dict__)