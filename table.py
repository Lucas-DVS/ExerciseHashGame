class Table:
    def __init__(self):

        self.__table = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    def table_view(self):  # Shows the table
        for li in range(0, 3):
            for c in range(0, 3):
                print(f'[{self.__table[li][c]:^10}]', end="  ")
            print()

    def table(self):
        return self.__table

    # Positions the value chosen by the user

    def setZero(self, zero):
        self.__table[0][0] = zero

    def getZero(self):
        return self.__table[0][0]

    def setOne(self, one):
        self.__table[0][1] = one

    def getOne(self):
        return self.__table[0][1]

    def setTwo(self, two):
        self.__table[0][2] = two

    def getTwo(self):
        return self.__table[0][2]

    def setThree(self, three):
        self.__table[1][0] = three

    def getThree(self):
        return self.__table[1][0]

    def setFour(self, four):
        self.__table[1][1] = four

    def getFour(self):
        return self.__table[1][1]

    def setFive(self, five):
        self.__table[1][2] = five

    def getFive(self):
        return self.__table[1][2]

    def setSix(self, six):
        self.__table[2][0] = six

    def getSix(self):
        return self.__table[2][0]

    def setSeven(self, seven):
        self.__table[2][1] = seven

    def getSeven(self):
        return self.__table[2][1]

    def setEight(self, eight):
        self.__table[2][2] = eight

    def getEight(self):
        return self.__table[2][2]
