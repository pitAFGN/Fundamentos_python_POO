class Temperatura:
    def __init__(self):
        self._celsius = 0

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, valor):
        if valor < -273.15:
            raise ValueError("La temperatura no puede ser menor que el cero absoluto")
        self._celsius = valor

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, valor):
        self.celsius = (valor - 32) * 5/9

temp = Temperatura()

temp.celsius = 25
print(f"{temp.celsius}°C = {temp.fahrenheit}°F")

temp.fahrenheit = 68
print(f"{temp.celsius}°C = {temp.fahrenheit}°F")

try:
    temp.celsius = -300
except ValueError as e:
    print(f"Error: {e}")