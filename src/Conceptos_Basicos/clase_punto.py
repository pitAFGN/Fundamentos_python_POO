class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Punto({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)

    def __eq__(self, otro):
        if not isinstance(otro, Punto):
            return False
        return self.x == otro.x and self.y == otro.y

    def __len__(self):
        return abs(self.x) + abs(self.y)

p1 = Punto(3, 4)
p2 = Punto(1, 2)

print(p1)
print(repr(p1))

p3 = p1 + p2
print(p3)

print(p1 == p2)
print(p1 == Punto(3, 4))

print(len(p1))