from rules import Rules
from player import Player


class Round:

    def __init__(self):

        self.__rule = Rules()  # Call class Rules
        self.__turn = 0  # Variable that controls whose turn it is
        self.__valueCheck = False  # Variable to control if the game input is valid
        self.__value = 0  # Variable with user choice
        self.__playing = True  # Infinite loop until game over
        self.__players = []  # List with the players

    def round(self, p1, p2):

        self.__players = [Player(p1), Player(p2)]
        self.__players[0].setSymbol("X")
        self.__players[1].setSymbol("O")
        self.__rule.matrizTolist()
        print()

        while self.__playing:

            print(
                f"It's {self.__players[self.__turn].getName()} turn. Your symbol is "
                f"{self.__players[self.__turn].getSymbol()} \n")
            self.__rule.getTabView()
            print()

            while not self.__valueCheck:  # Checking if player input is valid

                self.__value = input("Choose the number you want to place your symbol: ")
                print()

                self.__valueCheck = self.__value.isnumeric()
                if not self.__valueCheck:
                    print("Invalid input. You must choose a valid number")
                    print()
                elif self.__valueCheck:
                    self.__value = int(self.__value)
                    if (self.__value < 0) or (self.__value > 8):
                        print("Invalid Number. You must choose a valid number")
                        print()
                        self.__valueCheck = False
                    elif not self.__rule.invalidPosition(self.__value):
                        print("Invalid position. You must choose a valid number")
                        print()
                        self.__valueCheck = False
                    else:
                        break
                print(
                    f"It's {self.__players[self.__turn].getName()} turn. Your symbol is "
                    f"{self.__players[self.__turn].getSymbol()}")
                print()
                self.__rule.getTabView()
                print()

            self.__rule.placeSymbol(self.__value, self.__players[self.__turn].getSymbol())
            self.__rule.clearList()
            self.__rule.matrizTolist()

            # Checking if there was a winner.
            if self.__rule.winner(self.__players[self.__turn].getSymbol()):
                print(f'The winner is {self.__players[self.__turn].getName()}!')
                print(f'Used symbol {self.__players[self.__turn].getSymbol()}')
                print()
                self.__rule.getTabView()
                print()
                break

            # Validating if there was a tie.
            if not self.__rule.tie():
                print(f'Ended in a draw')
                print()
                self.__rule.getTabView()
                print()
                break

            self.__valueCheck = False  # Preparing the input control for the next round

            if self.__turn == 0:  # Round Control
                self.__turn = 1
            else:
                self.__turn = 0
