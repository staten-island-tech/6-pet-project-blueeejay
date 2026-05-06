# hero thingy but i added in a function similar to rolling a dice to determine species of character \
# eevery time i got lost on the API thing i came here and tried to add another function 
# my actual classword is in (prideotemp_l1.py), and my classes function notes is in firebird_l2.py
# each named after fictional warships from the same novel serena is from <333. the book series SUCKS though 
d6 = [1,2,3,4,5,6]
import random
class hero:
    def __init__(self, name, money, esteem, inventory, maxcap, heritage, fightskill): #max cap is unneccesary i just wanted to make the emotion system make more sense to me 
        self.name = name
        self.__money = money
        self.inventory = inventory
        self.__esteem = esteem
        self.heritage = heritage
        self.__maxcap = maxcap # the maximum confidence/positivity that hero can feel 
        self.__fightskill = fightskill

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

    # def skilltraining(self):
    #     print(self.name,"'s current skill level is:", self.__fightskill)
    #     for index, x in enumerate(self.inventory):
    #         print(index, ":", self.inventory[index])
    #     tool = int(input("Input the number corresponding to the type you are searching for:"))
    #     time = (input("In order to build this hero's skills with their chosen tool, you alot them [x] amount of hours to train. Type [x], the amount of hours, below:"))
    #     timeg = int(time)
    #     traininglog = []
    #     print(time)
    #     for range in (timeg):
    #          diceroll = int(random.choice(d6))
    #          traininglog.append(diceroll)
    #          print(diceroll, traininglog)
    #     if sum(traininglog) / timeg >= 4:
    #          self.__fightskill += 1 
    #          print("Their training session was successful! Their skill is now level", self.__fightskill)
    #     else: 
    #          print("Their training session was not incredibly productive, so their skill level has remained the same.")

         
         
    def bloodtest(self):
            print("You examine", self.name, "using a blood test to determine if they are 'touched' by the supernatural.")
            dicevalue = int(random.choice(d6)) 
            if (self.heritage).lower == "human":
                print("Your test is conclusive. You are able to determine", self.name, "has", self.heritage, "heritage, as expected!")
            elif dicevalue >= 5:
                print("Your test is conclusive. You are able to determine", self.name, "has", self.heritage , "heritage.")
            else:
                print("You are unable to determine the nature or type of their blood, but it's definitely unusual.")

    def checkin(self):
            print("You ask", self.name, "how they would define their confidence in their current work using numbers. They reply with",self.__esteem,"out of",self.__maxcap,".")

    def buy(self, item, x):
        self.inventory.append(item)
        self.__money = self.__money - x 
        print(self.name, "'s inventory currently has:", self.inventory)
        print(self.name, "spent", x, "and now has", self.__money, "credits remaining.")


Serena = hero("Serena D'Angelus",1400, 50, ["Palette Knife", "Pict-Recorder", 150],150, "Human", 2) # Heresy
Fulgrim = hero("Fulgrim of Chemos",52300,156, ["the Blade of the Laer", "the Fireblade", "Hairties","Stone Chisel", "plot armor"], 300, "Post-Human",5) # Heresy 
Kevin = hero("Kevin",0.45,300,["Radio"], 400, "Tremere, Kindred", 4) # Hunter: TP
Kitten = hero("Kitten", 43, 170, ["Ski Mask and Goggles","Homemade Polearm"], 200, "Human", 3) # HTP
Markus = hero("Markus", 0.53, 350, ["X-Box Controller","Stake Jacket", "Stilts-turned-Crutches"], 400, "Human, Mage", 4) # HTP 
Kevin.bloodtest()
# Markus.skilltraining()


""" Fulgrim = hero("Fulgrim of Chemos",52300,156, ["the Blade of the Laer", "the Fireblade", "Hairties","Stone Chisel", "plot armor"], 300)

Markus = hero("Markus", 0.53, 350, ["X-Box Controller","Stake Jacket", "Stilts-turned-Crutches"], 400)
Kitten = hero("Kitten", 43, 170, ["Ski Mask and Goggles","Homemade Polearm"], 200, "Human", 3) """