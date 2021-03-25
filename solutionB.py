class AbstractCat:
    def __init__(self):
        self.weight = 0
        self.store = 0

    def eat(self, food):
        if self.weight >= 100:
            return

        self.weight += (food + self.store) // 10
        self.store = (food + self.store) % 10

        self.weight = min(self.weight, 100)

    def __str__(self):
        return f'{type(self).__name__} ({self.weight})'


class Kitten(AbstractCat):
    def __init__(self, weight):
        super().__init__()
        self.weight = weight

    def meow(self):
        return 'meow...'

    def sleep(self):
        return 'Snore' * (self.weight // 5)


class Cat(Kitten):
    def __init__(self, weight, name):
        super().__init__(weight)
        self.name = name

    def meow(self):
        return super().meow().upper()

    def get_name(self):
        return self.name

    def catch_mice(self):
        return 'Got it!'

