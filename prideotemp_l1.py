
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


# serena d'angelus my goat ud be so much cooler if graham mcniel wasn't your author !!! and u happened to b dating his self insert... sighhhhh
#shes  under my custody now and the self insert character also. but he isnt a self insert for graham  

# activity 1 
class hero:
    def __init__(self, name, money, esteem, inventory, maxcap, species): #max cap is unneccesary i just wanted to make the emotion system make more sense to me 
        self.name = name
        self.__money = money
        self.inventory = inventory
        self.__esteem = esteem
        self.__maxcap = maxcap # the maximum confidence/positivity that hero can feel 

    def play(self):
        print(self.name, "is working on a new project. When defined numerically, their confidence in their work measures:", self.__esteem, "out of", self.__maxcap,".")
        compliment = (input("Tell them something about their current artwork:"))
        complimentp = len(compliment) * 2.5 

        if "perfect" in compliment or "vibrant" in compliment:
            self.__esteem = (complimentp + 15) + self.__esteem
        elif "yucky" in compliment or "uninspired" in compliment:
            self.__esteem =+ complimentp - 45
        else:
            self.__esteem += complimentp
        # THE ELSE SHOULD BE TRUE FOR MOST VALUES BUT THE FIRST ONE IS FOR ALL?? I DO NOT KNOW WHY ITS AN IF STATEMENT
        
        # max/min corrector. ensures the value is never negative or over self.__maxcap 
        if self.__esteem > self.__maxcap:
            self.__esteem = int(self.__maxcap)
        elif  self.__esteem < 0:
            self.__esteem = 0
    def interrogate(self, species):
        print("You examine", self.name, "to determine if they are 'touched' by the supernatural.")
        print("You a")
  
        
    def checkin(self):
        print("You ask", self.name, "how they would define their confidence in their current work using numbers. They reply with",self.__esteem,"out of",self.__maxcap,".")

    def buy(self, item, x):
        self.inventory.append(item)
        self.__money = self.__money - x 
        print(self.name, "'s inventory currently has:", self.inventory)
        print(self.name, "spent", x, "and now has", self.__money, "credits remaining.")

Serena = hero("Serena D'Angelus",1400, 50, ["Palette Knife", "Pict-Recorder", 150],150)
Serena.play()
Serena.checkin()

Ostian = hero("Ostian Delafor")
Fulgrim = hero("Fulgrim of Chemos",52300,156, ["the Blade of the Laer", "the Fireblade", "Hairties","Stone Chisel", "plot armor"], 300)
Aseneca = hero("Coralline Aseneca",12300,["Vox-Thief", "Fountain Pen Set"])

Markus = hero("Markus", 0.53, 350, ["X-Box Controller","Stake Jacket", "Stilts-turned-Crutches"], 400)
Kitten = hero("Kitten", 43, 170, ["Ski Mask and Goggles","Homemade Polearm"], 200)


