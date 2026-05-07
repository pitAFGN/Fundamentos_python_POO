# class Persona:
    # Aquí irá el código de la clase
#   pass

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Creamos un objeto Persona
ana = Persona("Ana García", 28)

# Creamos dos objetos Persona
ana = Persona("Ana García", 28)
juan = Persona("Juan López", 35)

# Accedemos a sus atributos
print(ana.nombre)
print(juan.edad)