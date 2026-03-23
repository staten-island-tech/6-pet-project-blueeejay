class hero:
    def __init__(self, name, money, esteem, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory
        self.__esteem = esteem

    def play():
        compliment = len(input("Tell Serena something NICE about her painting:"))
        print(compliment)
        complimentp = compliment * 1.5 
        esteem += complimentp

    def buy(self, item):
        self.inventory.append(item)
        print(self.name, "'s inventory currently has:", self.inventory)
Serena = hero("Serena",1400, 50, ["Palette Knife"])
# Serena.buy("Tyrian Purple Acrylic Paint")
Serena.play()
