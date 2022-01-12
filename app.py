class Shop:
    name = None
    SelectedItems = None
    qty = None
    products = None
    choice = None

    def __init__(self, prod):
        self.products = prod

    def sayHello(self):
        while not bool(self.name):
            self.name = input("Hello, what is your name? \n")

    def showMenu(self):
        print(f"Hello {self.name}! Please have a look at our Menu:")
        for i in product_list:
            print(i)

    def getChoice(self):
        while self.choice not in self.products:
            self.choice = input("Now please choose your product: \n").upper()

    def getqty(self):
        self.qty = input("Choose quantity: \n")
        while self.qty.isdigit() != True:
            self.qty = input("Choose only numbers! \n")

    def calculate(self):
        return self.products.get(self.choice) * float(self.qty)

    def showCalculate(self):
        print("Total sum of your product is {} USD.".format(self.calculate()))

    def Goodbye(self):
        print(f"Thank you {self.name} for visiting us. \nBy by!")


product_list = {

    "A": 2,
    "B": 3,
    "C": 4,
    "D": 5,
    "E": 6,
}

shop = Shop(product_list)
shop.sayHello()
shop.showMenu()
shop.getChoice()
shop.getqty()
shop.showCalculate()
shop.Goodbye()
