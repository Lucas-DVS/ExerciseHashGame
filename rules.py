from table import Table


class Rules:

    def __init__(self):

        self.__tab = Table()
        self.__list = []

    def matrizTolist(self):  # Transform the array into a list to check if anyone has won
        for lin in range(0, 3):
            for c in range(0, 3):
                y = self.__tab.table()
                self.__list.append(y[lin][c])

    def clearList(self):  # Clear the list for the next round check
        self.__list.clear()

    def winner(self, x):  # Validates if someone won
        if (self.__list[0] == x) and (self.__list[1] == x) and (self.__list[2] == x):
            return True
        elif (self.__list[3] == x) and (self.__list[4] == x) and (self.__list[5] == x):
            return True
        elif (self.__list[6] == x) and (self.__list[7] == x) and (self.__list[8] == x):
            return True
        elif (self.__list[0] == x) and (self.__list[3] == x) and (self.__list[6] == x):
            return True
        elif (self.__list[1] == x) and (self.__list[4] == x) and (self.__list[7] == x):
            return True
        elif (self.__list[2] == x) and (self.__list[5] == x) and (self.__list[8] == x):
            return True
        elif (self.__list[0] == x) and (self.__list[4] == x) and (self.__list[8] == x):
            return True
        elif (self.__list[2] == x) and (self.__list[4] == x) and (self.__list[6] == x):
            return True
        else:
            return False

    def getTabView(self):  # View the updated table
        self.__tab.table_view()

    def getList(self):
        print(self.__list)

    def placeSymbol(self, number, symbol):  # Assigns the value the user chose to the array
        if number == 0:
            self.__tab.setZero(symbol)
        elif number == 1:
            self.__tab.setOne(symbol)
        elif number == 2:
            self.__tab.setTwo(symbol)
        elif number == 3:
            self.__tab.setThree(symbol)
        elif number == 4:
            self.__tab.setFour(symbol)
        elif number == 5:
            self.__tab.setFive(symbol)
        elif number == 6:
            self.__tab.setSix(symbol)
        elif number == 7:
            self.__tab.setSeven(symbol)
        elif number == 8:
            self.__tab.setEight(symbol)

    def invalidPosition(self, position):  # Checks if the chosen position is valid
        if self.__list[position] == 'X':
            return False
        elif self.__list[position] == 'O':
            return False
        else:
            return True

    def tie(self):  # Valid if tied
        value = False
        for x in range(0, 9):
            if x in self.__list:
                value = True
        return value
