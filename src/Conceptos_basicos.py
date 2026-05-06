#concepto teorico de clase y objeto

#Ejemplo conceptual
class Libro:
    # Aquí definiremos atributos como título, autor, páginas
    # Y métodos como abrir(), leer(), cerrar()
    pass

# Creamos objetos (instancias) de la clase Libro
libro_python = Libro()  # Un libro específico sobre Python
novela_fantasia = Libro()  # Una novela de fantasía específica

#Ejemplo práctico: Modelando una biblioteca
class Libro:
    def __init__(self, titulo, autor, paginas, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.isbn = isbn
        self.disponible = disponible
        self.pagina_actual = 0  # Inicializamos en la página 0 (cerrado)

# Creamos algunos libros
libro1 = Libro("Python Crash Course", "Eric Matthes", 544, "9781593279288")
libro2 = Libro("Clean Code", "Robert C. Martin", 464, "9780132350884", False)

# Verificamos si están disponibles
print(f"{libro1.titulo} está {'disponible' if libro1.disponible else 'prestado'}")
print(f"{libro2.titulo} está {'disponible' if libro2.disponible else 'prestado'}")

#Ejemplo práctico: Biblioteca
class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.pagina_actual = 0
        self.abierto = False

    def abrir(self):
        if self.abierto:
            return f"{self.titulo} ya está abierto"
        self.abierto = True
        return f"{self.titulo} ha sido abierto"

    def cerrar(self):
        if not self.abierto:
            return f"{self.titulo} ya está cerrado"
        self.abierto = False
        return f"{self.titulo} ha sido cerrado"

    def leer(self, num_paginas):
        if not self.abierto:
            return f"No puedes leer: {self.titulo} está cerrado"

        if self.pagina_actual >= self.paginas:
            return f"Ya has terminado de leer {self.titulo}"

        paginas_restantes = self.paginas - self.pagina_actual
        paginas_a_leer = min(num_paginas, paginas_restantes)

        self.pagina_actual += paginas_a_leer

        if self.pagina_actual >= self.paginas:
            return f"Has leído {paginas_a_leer} páginas y has terminado {self.titulo}"

        return f"Has leído {paginas_a_leer} páginas. Estás en la página {self.pagina_actual} de {self.paginas}"

    def reiniciar_lectura(self):
        self.pagina_actual = 0
        return f"Has reiniciado la lectura de {self.titulo}"

    def __str__(self):
        estado = "abierto" if self.abierto else "cerrado"
        progreso = f"{self.pagina_actual}/{self.paginas} páginas"
        return f"{self.titulo} por {self.autor} - {progreso} - {estado}"