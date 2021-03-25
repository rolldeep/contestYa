class Robot:
    def __init__(self, position):
        self.x, self.y = position
        self.d = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}
        self.moves = [position]

    def move(self, s):
        self.moves = [(self.x, self.y)]
        for direction in s:
            dx, dy = self.d[direction]
            self.x += dx
            self.y += dy
            self.moves.append((self.x, self.y))
        return self.moves[-1]

    def path(self):
        return self.moves
