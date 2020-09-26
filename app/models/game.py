class Game:

def __init__(self, player_1, player_2):
    self.player_1 = player_1
    self.player_2 = player_2

def find_winner(self, player_1, player_2):
    if self.player_1.choice == self.player_2.choice:
        return "It's a draw!"
    elif self.player_1.choice == "rock" and self.player_2.choice == "paper":
        return f"{player_2.name} wins! Paper covers rock!"
    elif self.player_1.choice == "rock" and self.player_2.choice == "scissors":
        return f"{player_1.name} wins! Rock bashes scissors!"
    elif self.player_1.choice == "paper" and self.player_2.choice == "rock":
        return f"{player_1.name}" wins! Paper covers rock!"
    elif self.player_1.choice == "paper" and self.player_1.choice == "scissors":
        return f"{player_2.name} wins! Scissors cut paper!"
    elif self.player_1.choice == "scissors" and self.player_2.choice == "rock":
        return f"{player_2.name} wins! Rock bashes scissors!"
    elif self.player_1.choice == "scissors" and self.player_2.choice == "paper":
        return f"{player_1.name} wins! Scissors cut paper!"
    
    

    
        

        