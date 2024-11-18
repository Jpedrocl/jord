class Character:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level
        self.points = 0
        self.position = 0

    def move(self, steps):
        self.position += steps

    def add_points(self, points):
        self.points += points

    def get_info(self):
        return f"{self.name} (Nível {self.level}) - Pontos: {self.points}, Posição: {self.position}"

    def __str__(self):
        return self.get_info()
