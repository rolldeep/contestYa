class PearsBasket:
    def __init__(self, pears):
        self.pears = pears

    def __floordiv__(self, n):
        c = self.pears // n
        left = self.pears % n
        return [PearsBasket(c)
                for _ in range(n)] + ([PearsBasket(left)] if left else [])

    def __mod__(self, n):
        return self.pears % n

    def __add__(self, other):
        return PearsBasket(self.pears + other.pears)

    def __sub__(self, n):
        self.pears = max(self.pears - n, 0)

    def __repr__(self):
        return f'{type(self).__name__}({self.pears})'

    def __str__(self):
        return str(self.pears)
