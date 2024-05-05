import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Computer")

    def start(self):
        while self.player.is_alive() and self.computer.is_alive():
            # Player's turn
            print(f"{self.player.name} attacks {self.computer.name}")
            self.player.attack(self.computer)
            print(f"{self.computer.name}'s health: {self.computer.health}")

            if not self.computer.is_alive():
                print(f"{self.player.name} wins!")
                break

            # Computer's turn
            print(f"{self.computer.name} attacks {self.player.name}")
            self.computer.attack(self.player)
            print(f"{self.player.name}'s health: {self.player.health}")

            if not self.player.is_alive():
                print(f"{self.computer.name} wins!")

if __name__ == "__main__":
    player_name = input("Enter your hero's name: ")
    game = Game(player_name)
    game.start()