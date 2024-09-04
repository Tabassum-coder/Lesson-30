class myClass:
    __privVar=10

    def __privMeth(self):
        print("This is a private method")
    
    def Hello(self):
        print(self.__privVar)

m1=myClass()

m1.Hello()
m1.__privMeth()