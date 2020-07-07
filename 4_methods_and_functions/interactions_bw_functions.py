# create a program which
from random import shuffle

class ThreeCupMonte():
    def __init__(self):
        self.monte = ['O','','']

    def shuffle(self):
        shuffle(self.monte)
        return self.monte

    def player_choice(self, choice):
        choice = int(choice) - 1
        self.shuffle()
        print(f'monte: {self.monte}')
        print(f'your choice: {choice}')
        # return self.monte[choice] == 'O'
        return 'You won! :)' if self.monte[choice] == 'O' else 'You lost :('

game = ThreeCupMonte()

result = input("Pick a number between 1 and 3:\n")
print(game.player_choice(result))
