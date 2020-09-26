import unittest
from app.models.game import Game
from app.models.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player("Player 1", "rock")
        self.player_2 = Player("Player 2", "scissors")
        self.game_1 = Game(self.player_1, self.player_2)

    def test_can_find_winner(self):
        self.assertEqual(self.player_1, self.game_1.find_winner(self.player_1, self.player_2))
