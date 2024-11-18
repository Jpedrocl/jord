class Ranking:
    def __init__(self):
        self.ranking = {}

    def update(self, player):
        self.ranking[player.name] = player.points

    def display(self):
        sorted_ranking = sorted(self.ranking.items(), key=lambda x: x[1], reverse=True)
        print("\n=== Ranking Atual ===")
        for i, (name, points) in enumerate(sorted_ranking, 1):
            print(f"{i}. {name}: {points} pontos")
