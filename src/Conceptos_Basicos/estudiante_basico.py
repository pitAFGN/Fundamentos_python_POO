class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.activo = True

estudiante1 = Estudiante("María", 20)
estudiante2 = Estudiante("Carlos", 22)

print(estudiante1.nombre)
print(estudiante2.nombre)