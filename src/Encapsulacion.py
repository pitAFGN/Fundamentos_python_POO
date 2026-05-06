#Encapsulación

#Ejemplo práctico: Clase Producto
class Producto:
    def __init__(self, nombre, precio, stock=0):
        self._nombre = nombre
        self._precio = precio
        self._stock = stock
        self._descuento = 0

    # Getters
    def get_nombre(self):
        return self._nombre

    def get_precio(self):
        # Aplicamos el descuento al devolver el precio
        return self._precio * (1 - self._descuento)

    def get_precio_base(self):
        # Devolvemos el precio sin descuento
        return self._precio

    def get_stock(self):
        return self._stock

    def get_descuento(self):
        return self._descuento

    # Setters
    def set_nombre(self, nuevo_nombre):
        if not isinstance(nuevo_nombre, str) or len(nuevo_nombre) == 0:
            raise ValueError("El nombre debe ser una cadena no vacía")
        self._nombre = nuevo_nombre

    def set_precio(self, nuevo_precio):
        if not isinstance(nuevo_precio, (int, float)) or nuevo_precio < 0:
            raise ValueError("El precio debe ser un número positivo")
        self._precio = nuevo_precio

    def set_stock(self, nuevo_stock):
        if not isinstance(nuevo_stock, int) or nuevo_stock < 0:
            raise ValueError("El stock debe ser un entero positivo")
        self._stock = nuevo_stock

    def set_descuento(self, nuevo_descuento):
        if not isinstance(nuevo_descuento, float) or not 0 <= nuevo_descuento <= 1:
            raise ValueError("El descuento debe ser un número entre 0 y 1")
        self._descuento = nuevo_descuento

#Ejemplo: Procesamiento de datos en etapas
class ProcesadorTexto:
    def __init__(self):
        self._texto = ""
        self._estadísticas = {}

    def procesar_archivo(self, ruta_archivo):
        """Método público que procesa un archivo de texto."""
        try:
            texto = self.__leer_archivo(ruta_archivo)
            self._texto = self.__normalizar_texto(texto)
            self._estadísticas = self.__calcular_estadísticas(self._texto)
            return True
        except Exception as e:
            print(f"Error al procesar el archivo: {e}")
            return False

    def __leer_archivo(self, ruta):
        """Método privado para leer el contenido de un archivo."""
        with open(ruta, 'r', encoding='utf-8') as archivo:
            return archivo.read()

    def __normalizar_texto(self, texto):
        """Método privado para normalizar el texto."""
        # Convertir a minúsculas
        texto = texto.lower()
        # Eliminar caracteres especiales
        import re
        texto = re.sub(r'[^\w\s]', '', texto)
        # Eliminar espacios extra
        texto = re.sub(r'\s+', ' ', texto).strip()
        return texto

    def __calcular_estadísticas(self, texto):
        """Método privado para calcular estadísticas del texto."""
        palabras = texto.split()
        estadísticas = {
            'total_palabras': len(palabras),
            'palabras_únicas': len(set(palabras)),
            'longitud_promedio': sum(len(p) for p in palabras) / len(palabras) if palabras else 0
        }
        return estadísticas

    def obtener_estadísticas(self):
        """Método público para acceder a las estadísticas calculadas."""
        return self._estadísticas.copy()

    def obtener_texto_procesado(self):
        """Método público para obtener el texto procesado."""
        return self._texto

#Ejemplo práctico: Validación de datos complejos
class Formulario:
    def __init__(self):
        self._datos = {}
        self._errores = {}

    def validar(self, datos):
        """Método público para validar todos los datos del formulario."""
        self._datos = datos.copy()
        self._errores = {}

        # Usar métodos privados para cada tipo de validación
        self.__validar_campos_requeridos()
        self.__validar_email()
        self.__validar_contraseña()
        self.__validar_edad()

        return len(self._errores) == 0

    def obtener_errores(self):
        """Método público para obtener los errores de validación."""
        return self._errores.copy()

    def __validar_campos_requeridos(self):
        """Método privado para validar campos obligatorios."""
        campos_requeridos = ['nombre', 'email', 'contraseña']
        for campo in campos_requeridos:
            if campo not in self._datos or not self._datos[campo]:
                self._errores[campo] = f"El campo {campo} es obligatorio"

    def __validar_email(self):
        """Método privado para validar formato de email."""
        if 'email' in self._datos and self._datos['email']:
            import re
            patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(patron, self._datos['email']):
                self._errores['email'] = "El formato del email no es válido"

    def __validar_contraseña(self):
        """Método privado para validar seguridad de contraseña."""
        if 'contraseña' in self._datos and self._datos['contraseña']:
            contraseña = self._datos['contraseña']
            if len(contraseña) < 8:
                self._errores['contraseña'] = "La contraseña debe tener al menos 8 caracteres"
            elif not any(c.isupper() for c in contraseña):
                self._errores['contraseña'] = "La contraseña debe contener al menos una mayúscula"
            elif not any(c.isdigit() for c in contraseña):
                self._errores['contraseña'] = "La contraseña debe contener al menos un número"

    def __validar_edad(self):
        """Método privado para validar la edad."""
        if 'edad' in self._datos:
            try:
                edad = int(self._datos['edad'])
                if edad < 18:
                    self._errores['edad'] = "Debes ser mayor de edad"
                elif edad > 120:
                    self._errores['edad'] = "La edad ingresada no es válida"
            except ValueError:
                self._errores['edad'] = "La edad debe ser un número"

