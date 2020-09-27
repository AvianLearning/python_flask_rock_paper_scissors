from random import choice

class Computer:
    
    def __init__ (self, name, weapon):
        self.name = name
        weapon_list = ["rock", "paper", "scissors"]
        self.weapon = choice(weapon_list) 
