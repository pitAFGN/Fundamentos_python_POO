class Estudiante:
    universidad = "Universidad Autónoma"

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

estudiante1 = Estudiante("María", 20)
estudiante2 = Estudiante("Carlos", 22)

print(estudiante1.universidad)
print(estudiante2.universidad)
print(Estudiante.universidad)

Estudiante.universidad = "Universidad Complutense"

print(estudiante1.universidad)
print(estudiante2.universidad)