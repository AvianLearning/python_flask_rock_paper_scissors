import unittest
from app.models.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player("Player 1", "Rock")
        self.player_2 = Player("Player 2", "Scissors")
    

    def test_can_find_player_by_name(self):
        self.assertEqual("Player 1", self.player_1.name)
    
    def test_can_find_player_choice(self):
        self.assertEqual("Scissors", self.player_2.choice)