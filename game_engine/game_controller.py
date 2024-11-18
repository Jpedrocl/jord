from characters.warrior import Warrior
from characters.mage import Mage
from characters.archer import Archer
from game_engine.dice import Dice
from game_engine.map import Map
from game_engine.ranking import Ranking
from game_config.settings import DEFAULT_MAP_SIZE, DEFAULT_ROUNDS

class RPGGame:
    def __init__(self):
        self.players = []
        self.map = None
        self.dice = Dice()
        self.ranking = Ranking()
        self.rounds = 0

    def setup_game(self):
        print("=== Configuração do Jogo ===")
        num_players = int(input("Digite o número de jogadores: "))
        for _ in range(num_players):
            name = input("Digite o nome do jogador: ")
            print("Escolha uma classe: 1. Guerreiro, 2. Mago, 3. Arqueiro")
            class_choice = int(input("Digite o número da classe: "))
            if class_choice == 1:
                self.players.append(Warrior(name))
            elif class_choice == 2:
                self.players.append(Mage(name))
            elif class_choice == 3:
                self.players.append(Archer(name))
            else:
                print("Classe inválida! Escolhendo Guerreiro como padrão.")
                self.players.append(Warrior(name))

        map_size = int(input(f"Digite o tamanho do mapa (Padrão {DEFAULT_MAP_SIZE}): ") or DEFAULT_MAP_SIZE)
        self.map = Map(map_size)
        self.rounds = int(input(f"Digite o número de rodadas (Padrão {DEFAULT_ROUNDS}): ") or DEFAULT_ROUNDS)

    def play_round(self):
        for player in self.players:
            print(f"\n=== Turno de {player.name} ===")
            input("Pressione Enter para jogar o dado...")
            roll = self.dice.roll()
            print(f"{player.name} rolou um {roll}!")
            player.move(roll)
            message = self.map.get_message(player.position)
            print(f"Mensagem da casa {player.position}: {message}")
            points_earned = random.randint(1, 10)
            print(f"{player.name} ganhou {points_earned} pontos!")
            player.add_points(points_earned)
            self.ranking.update(player)

    def play_game(self):
        print("\n=== Início do Jogo ===")
        for round_number in range(1, self.rounds + 1):
            print(f"\n=== Rodada {round_number}/{self.rounds} ===")
            self.play_round()
            self.ranking.display()

        print("\n=== Jogo Finalizado ===")
        self.ranking.display()
