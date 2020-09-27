import unittest
from app.models.game import Game
from app.models.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player("Player 1", "rock")
        self.player_2 = Player("Player 2", "scissors")
        self.player_3 = Player("Player 3", "paper")
        self.player_4 = Player("Player 4", "paper")
        self.game_1 = Game(self.player_1, self.player_2)
        self.game_2 = Game(self.player_3, self.player_4)
        self.game_3 = Game(self.player_2, self.player_3)
        self.game_4 = Game(self.player_1, self.player_3)

    def test_can_find__winner_rock_scissors(self):
        self.assertEqual(self.player_1, self.game_1.find_winner(self.player_1, self.player_2))

    def test_can_find_a_draw(self):
        self.assertEqual(None, self.game_2.find_winner(self.player_3, self.player_4))

    def test_can_find__winner_scissors_paper(self):
        self.assertEqual(self.player_2, self.game_3.find_winner(self.player_2, self.player_3))

    def test_can_find_winner_paper_rock(self):
        self.assertEqual(self.player_3, self.game_4.find_winner(self.player_1, self.player_3))

    def test_can_find_computer_name(self):
        weapon = computer_choice()
        computer_player = Player("Computer", weapon)

