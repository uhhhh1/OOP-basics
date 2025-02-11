class Fruit: 
    def __init__(self, name, color, lebron, price):
        self.name = name
        self.color = color
        self.lebron = lebron 
        self.price = float(price)
    
    #Prints fruit details 
    def details(self):
        print(f"""
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            Fruit Type: {self.name}
            Fruit Color: {self.color}
            Fruit's Favorite Basketball Player: {self.lebron}
            Fruit Price: {self.price}
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """)

    def calc_sales_tax(self, tax):
        total = (self.price*tax) + self.price
        print(f"""
        ~~~~~~~~~~~~~~~~~~~~~
        Total cost of {self.name}: {total}
        ~~~~~~~~~~~~~~~~~~~~~
        """)


apple = Fruit("Apple", "Red", "Lebron", "1.25")
pear = Fruit("Pear", "Green", "Lebron", "1.50")
strawberry = Fruit("Strawberry", "Red", "Lebron", "3.75")

apple.details()
pear.details()
strawberry.details()

apple.calc_sales_tax(0.4)