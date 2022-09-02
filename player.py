class Player:

    def __init__(self, name):
        self.__name = name
        self.__symbol = ''

    def getName(self):
        return self.__name

    def setSymbol(self, symbol):
        self.__symbol = symbol

    def getSymbol(self):
        return self.__symbol
