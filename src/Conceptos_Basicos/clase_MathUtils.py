class MathUtils:
    @staticmethod
    def es_primo(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    @staticmethod
    def factorial(n):
        if n < 0:
            raise ValueError("El factorial no está definido para números negativos")
        if n == 0 or n == 1:
            return 1
        return n * MathUtils.factorial(n - 1)

print(MathUtils.es_primo(17))
print(MathUtils.es_primo(20))
print(MathUtils.factorial(5))