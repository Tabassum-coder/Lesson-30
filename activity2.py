class Computer:

    def __init__(self):
        self.__max_price=900
    def Sell(self):
        print("Selling price is",self.__max_price)
    def setMaxPrice(self,price):
        self.__max_price=price
        
c=Computer()
c.Sell()

c.__max_price=1000
c.Sell()

c.setMaxPrice(1000)
c.Sell()