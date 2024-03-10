class Product:
    def __init__(self,pid,name,price,desc, quantity):
        self.__pid=pid
        self.name=name
        self.price=price
        self.desc=desc
        self.quantity=quantity

    def display(self):
        print("PID: ", self.__pid)
        print("NAME: ", self.name)
        print("PRICE: ", self.price)
        print("DESCRIPTION: ", self.desc)
        print("QUANTITY: ", self.quantity)

    def updatePid(self, pid):
        self.__pid = pid

    def updateName(self, name):
        self.name = name

    def updatePrice(self, price):
        self.price = price

    def updateDesc(self, desc):
        self.desc = desc
    
    def updateQuantity(self, quantity):
        self.quantity = quantity

    def getPID(self):
        return self.__pid
