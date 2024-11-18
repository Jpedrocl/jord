import unittest
from game_engine.game_controller import RPGGame

class TestRPGGame(unittest.TestCase):
    def test_setup_game(self):
        game = RPGGame()
        game.setup_game()
        self.assertTrue(len(game.players) > 0)

    def test_roll_dice(self):
        dice = Dice()
        roll = dice.roll()
        self.assertGreaterEqual(roll, 1)
        self.assertLessEqual(roll, 6)

    def test_ranking_update(self):
        player = Warrior("Test Player")
        player.add_points(10)
        ranking = Ranking()
        ranking.update(player)
        self.assertIn("Test Player", ranking.ranking)

if __name__ == "__main__":
    unittest.main()
