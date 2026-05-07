class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

p = Persona("Laura", 29)

print(hasattr(p, "nombre"))
print(hasattr(p, "apellido"))

print(getattr(p, "nombre"))
print(getattr(p, "apellido", "No especificado"))

setattr(p, "apellido", "García")
print(p.apellido)

delattr(p, "apellido")