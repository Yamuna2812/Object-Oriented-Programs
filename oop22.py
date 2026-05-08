class ATM:
    def __init__(self):
        self.__pin = 1234

    def access(self):
        print(self.__pin)

obj = ATM()
obj.access()
