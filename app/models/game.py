from random import choice 

class Game:

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def find_winner(self, player_1, player_2):
        if self.player_1.choice == self.player_2.choice:
            return None
        elif self.player_1.choice == "rock" and self.player_2.choice == "paper":
            return player_2
        elif self.player_1.choice == "rock" and self.player_2.choice == "scissors":
            return player_1
        elif self.player_1.choice == "paper" and self.player_2.choice == "rock":
            return player_1
        elif self.player_1.choice == "paper" and self.player_2.choice == "scissors":
            return player_2
        elif self.player_1.choice == "scissors" and self.player_2.choice == "rock":
            return player_2
        elif self.player_1.choice == "scissors" and self.player_2.choice == "paper":
            return player_1
    
    # def computer_choice(self):
    #     weapon_list = ["rock", "paper", "scissors"]
    #     self.weapon = choice(weapon_list) 
    #     return self.weapon



       

        