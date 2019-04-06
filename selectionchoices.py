class SelectionChoices():
    def __init__(self):
        self.__dateChoice = 0
        self.__categoryChoice = 0

    def clearFields(self):
        self.__dateChoice = 0
        self.__categoryChoice = 0

    def getAllFields(self):
        return {'DateChoice':self.__dateChoice, \
                'CategoryChoice':self.__categoryChoice
                }

    def setDateChoice(self, buttonId):
        self.__dateChoice = buttonId

    def getDateChoice(self):
        return self.__dateChoice

    def setCategoryChoice(self, buttonId):
        self.__categoryChoice = buttonId

    def getCategoryChoice(self):
        return self.__categoryChoice