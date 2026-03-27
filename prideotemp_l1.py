
#Calculator Code
""" class Calculator():
    def add(x, y):
        print(x + y)
        return x + y

    def add_many(numbers):
        print(sum(numbers))
        return sum(numbers)

    def subtract(numbers):
        return numbers

Calculator.add(5, 6) """
# creating a hero
""" class Hero:
    def __init__(self, name, money, inventory):  # init sets up starting info 
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory) 

Jillian = Hero("Jillian", 150, ["Potion"])

Jillian.buy({"title": "Sword", "atk": 34})
print(Jillian.__dict__) """
# encapsulationnn
 # double underscore means "private"

# ACTIVITY TIME!! !ACTITIVY 1 
""" 
class hero:
    def __init__(self, name, money, esteem, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory
        self.__esteem = esteem
        

    def buy(self, item, x):
        self.inventory.append(item)
        self.money = self.money - x # also unnecessary </3 i really enjoy this activity 
        print(self.name, "'s inventory currently has:", self.inventory)
        print(self.name, "spent", x, "and now has", self.money, "credits remaining.") # this was unnecessary i also just wanted to do this. you cant buy things for free even though thatd be awesome 

Serena = hero("Serena",1400, 50, ["Palette Knife"])
Serena.buy("Tyrian Purple Acrylic Paint", 45)  """

# activity 1 
class hero:
    def __init__(self, name, money, esteem, inventory, maxcap): #max cap is unneccesary i just wanted to make the emotion system make more sense to me 
        self.name = name
        self.__money = money
        self.inventory = inventory
        self.__esteem = esteem
        self.__maxcap = maxcap # the maximum confidence/positivity that hero can feel 

    def play(self):
        print(self.name, "is working on a new project. When defined numerically, their confidence in their work measures:", self.__esteem, "out of", self.__maxcap,".")
        compliment = (input("Tell them something about their current artwork:"))
        complimentp = len(compliment) * 1.5 
        self.__esteem += complimentp
        if "perfect" or "vibrant" in compliment:
            complimentp += 15 
        if "yucky" or "uninspired" in compliment:
            complimentp -= 45 
        if self.__esteem > self.__maxcap:
            self.__esteem = int(self.__maxcap)
            print(complimentp,self.__maxcap)
        
    def checkin(self):
        print("You ask", self.name, "how they would define their confidence in their current work using numbers. They reply with", self.__esteem,"out of", self.__maxcap,".")
        

    def buy(self, item, x):
        self.inventory.append(item)
        self.__money = self.__money - x 
        print(self.name, "'s inventory currently has:", self.inventory)
        print(self.name, "spent", x, "and now has", self.__money, "credits remaining.")

Serena = hero("Serena",1400, 50, ["Palette Knife"], 150)
Serena.play()
Serena.checkin()
