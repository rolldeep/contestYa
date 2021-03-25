class Vehicle:
    def __init__(self, num, speed):
        self.num = num
        self.speed = speed

    def positionAt(self, M, t):
        # return (M - self.speed * t % M) % M
        d1 = (M - (self.speed * t) % M) % M
        d2 = (self.speed * t) % M
        return min(d1, d2)


class Car(Vehicle):
    def __init__(self, num, speed, fuel):
        super().__init__(num, self.adjusted_speed(speed, fuel))

    def adjusted_speed(self, speed, fuel):
        if fuel == 95:
            return speed * 0.9
        elif fuel == 92:
            return speed * 0.8
        return speed


class Motorcycle(Vehicle):
    def __init__(self, num, speed, fuel):
        super().__init__(num, self.adjusted_speed(speed, fuel))

    def adjusted_speed(self, speed, fuel):
        if fuel == 95:
            return speed * 0.8
        elif fuel == 92:
            return speed * 0.6
        return speed


class Coach(Vehicle):
    pass


if __name__ == "__main__":
    n, M, t = [int(x) for x in input().split(' ')]
    vehicles = []
    for _ in range(n):
        num, type_v, speed, *fuel = [int(x) for x in input().split(' ')]

        if type_v == 1:
            vehicles.append(Car(num, speed, fuel[0]))
        if type_v == 2:
            vehicles.append(Motorcycle(num, speed, fuel[0]))
        if type_v == 3:
            vehicles.append(Coach(num, speed))

    print(min([(v.positionAt(M, t), v.num) for v in vehicles])[1])
