# Sahir Mukadam
# Assignment 10.1: Your Own Class
# This script is intended to create a class about skin and skincare by looking at traits and changing them depending on products used.

import random

class Skincare:
    #As long as you're trying to improve (the purpose of this class in the first place), you're always doing great on progress.
    progress = 10
    
    #Create a constructor featuring five traits: how much acne one has, how well one's skin glows, how hydrated one's skin is, how wrinkly one's skin is, and how soft one's skin is.
    def __init__(self):
        
        self.__money = 300
        self.__acne = random.randint(1, 10)
        self.__glow = random.randint(1, 10)
        self.__hydration = random.randint(1, 10)
        self.__wrinkles = random.randint(1, 10)
        self.__texture = random.randint(1, 10)

    #The money variable represents how much money one has to buy skincare products.
    def get_money(self):
        return self.__money

    #The acne variable represents how bad someone's acne is on a scale from 1 (major breakouts) to 10 (clear skin).
    def get_acne(self):
        return self.__acne

    #The glow variable represents how nice someone's skin glow is on a scale from 1 (dull skin) to 10 (natural luster).
    def get_glow(self):
        return self.__glow

    #The hydration variable represents how nice someone's skin's glow is on a scale from 1 (dull skin) to 10 (natural luster).
    def get_hydration(self):
        return self.__hydration

    #The wrinkles variable represents how wrinkly someone's skin from 1 (aged) to 10 (youthful).
    def get_wrinkles(self):
        return self.__wrinkles

    #The texture variable represents how soft someone's skin is from 1 (rough) to 10 (soft).
    def get_texture(self):
        return self.__texture
    
    def set_money(self, price):
        self.__money -= price

    #This improves one's acne stat, bringing them closer to 10.
    def set_acne(self):
        if self.__acne < 10:
            self.__acne += 1

    #This improves one's glow stat, bringing them closer to 10.
    def set_glow(self):
        if self.__glow < 10:
            self.__glow += 1

    #This improves one's hydration stat, bringing them closer to 10.
    def set_hydration(self):
        if self.__hydration < 10:
            self.__hydration += 1

    #This improves one's wrinkles stat, bringing them closer to 10.
    def set_wrinkles(self):
        if self.__wrinkles < 10:
            self.__wrinkles += 1

    #This improves one's texture stat, bringing them closer to 10.
    def set_texture(self):
        if self.__texture < 10:
            self.__texture += 1

    #This offers a random free skincare product, thus increasing the stats relating to the random skincare product.
    def voucher(self):
        #Receiving a free skincare product has a 10% chance of happening, aka if the number 10 is chosen.
        causeorno = random.randint(1,3)
        if causeorno == 10:
            chooseitem = random.randint(1,9)
            #1 provides the effects of salicylic acid.
            if chooseitem == 1:
                print("You have received a free bottle of salicylic acid, helping your acne, glow, and texture!")
            #2 provides the effects of hyaluronic acid.
            if chooseitem == 2:
                print("You have received a free bottle of hyaluronic acid, helping your hydration and wrinkles!")
            #3 provides the effects of glycolic acid.
            if chooseitem == 3:
                print("You have received a free bottle of glycolic acid, helping your acne, glow, wrinkles, and texture!")
            #4 provides the effects of lactic acid.
            if chooseitem == 4:
                print("You have received a free bottle of lactic acid, helping your acne, glow, hydration, wrinkles, and texture!")
            #5 provides the effects of mandelic acid.
            if chooseitem == 5:
                print("You have received a free bottle of mandelic acid, helping your acne, glow, wrinkles, and texture!")
            #6 provides the effects of azelaic acid.
            if chooseitem == 6:
                print("You have received a free bottle of azelaic acid, helping your acne, glow, and texture!")
            #7 provides the effects of ferulic acid.
            if chooseitem == 7:
                print("You have received a free bottle of ferulic acid, helping your glow and wrinkles!")
            #8 provides the effects of kojic acid.
            if chooseitem == 8:
                print("You have received a free bottle of kojic acid, helping your acne and glow!")
            #9 provides the effects of L-ascorbic acid.
            if chooseitem == 9:
                print("You have received a free bottle of L-ascorbic acid, helping your glow, hydration, and wrinkles!")
    
    #This causes a breakout, and a loss in a random stat.
    def breakout(self):
        #A breakout has a 25% chance of occurring, aka if the number 4 is chosen.
        causeorno = random.randint(1, 3)
        if causeorno == 4:
            typeofloss = random.randint(1, 5)
            #1 corresponds to a decrease in the acne stat.
            if typeofloss == 1:
                print("Your acne has flared up, reducing the stat by one!\n")
                self.__acne -= 1
            #2 corresponds to a decrease in the glow stat.
            elif typeofloss == 2:
                print("Your skin seems duller than before, reducing the stat by one!\n")
                self.__glow -= 1
            #3 corresponds to a decrease in the hydration stat.
            elif typeofloss == 3:
                print("Your skin has become drier than before, reducing the stat by one!\n")
                self.__hydration -= 1
            #4 corresponds to a decrease in the wrinkles stat.
            elif typeofloss == 4:
                print("Your skin has gained some wrinkles, reducing the stat by one!\n")
                self.__wrinkles -= 1
            #5 corresponds to a decrease in the texture stat.
            elif typeofloss == 5:
                print("Your skin seems rougher than before, reducing the stat by one!\n")
                self.__texture -= 1

def main():
    derm = Skincare()

    #Check to make sure that you are not broke, and that you do not have perfect stats yet.
    while derm.get_money() > 19 and derm.get_acne() + derm.get_glow() + derm.get_hydration() + derm.get_wrinkles() + derm.get_texture() < 50:
        #List the skincare products and prices.
        print("What skincare product would you like to buy? Type any of the following lowercase to buy it!")
        print("salicylic, hyaluronic, glycolic, lactic, mandelic, azelaic, ferulic, kojic, ascorbic")
        print("The prices respectively are $20, $28, $24, $39, $25, $22, $21, $29, and $26.")
        #List how much money there is left to spend.
        print(f"You have ${derm.get_money()} left to spend.")
        #Display one's current stats.
        print("Your stats for your skin are as following, ranging from 1 to 10, with 10 being the ideal level.")
        print(f"Acne: {derm.get_acne()}, Glow: {derm.get_glow()}, Hydration: {derm.get_hydration()}, Wrinkles: {derm.get_wrinkles()}, and Texture: {derm.get_texture()}.")
        payment = input("Buy: ")
        
        #If they asked for salicylic acid:
        if payment == "salicylic":
            print("You bought a bottle of salicylic acid for $20! This will help your skin's acne, glow, and texture!\n")
            #Check that they have enough money.
            if derm.get_money() >= 20:
                #Remove $20 from one's money.
                derm.set_money(20)
                #Increase one's acne, glow, and texture stats.
                derm.set_acne()
                derm.set_glow()
                derm.set_texture()
                #Trigger a possible breakout.
                derm.breakout()
                #Raise the possibility of a free product.
                derm.voucher()

        #If they asked for hyaluronic acid:
        elif payment == "hyaluronic":
            print("You bought a bottle of hyaluronic acid for $28! This will help your skin's hydration and wrinkles!\n")
            #Check that they have enough money.
            if derm.get_money() >= 28:
                #Remove $28 from one's money.
                derm.set_money(28)
                #Increase one's hydration and wrinkles stats.
                derm.set_hydration()
                derm.set_wrinkles()
                #Trigger a possible breakout.
                derm.breakout()
                #Raise the possibility of a free product.
                derm.voucher()

        #If they asked for glycolic acid:
        elif payment == "glycolic":
            print("You bought a bottle of glycolic acid for $24! This will help your skin's acne, glow, wrinkles, and texture!\n")
            #Check that they have enough money.
            if derm.get_money() >= 24:
                #Remove $24 from one's money.
                derm.set_money(24)
                #Increase one's acne, glow, wrinkles, and texture stats.
                derm.set_acne()
                derm.set_glow()
                derm.set_wrinkles()
                derm.set_texture()
                #Trigger a possible breakout.
                derm.breakout()
                #Raise the possibility of a free product.
                derm.voucher()

        #If they asked for lactic acid:
        elif payment == "lactic":
            print("You bought a bottle of lactic acid for $39! This will help your skin's acne, glow, hydration, wrinkles, and texture!\n")
            #Check that they have enough money.
            if derm.get_money() >= 39:
                #Remove $39 from one's money.
                derm.set_money(39)
                #Increase all of one's stats.
                derm.set_acne()
                derm.set_glow()
                derm.set_hydration()
                derm.set_wrinkles()
                derm.set_texture()
                #Trigger a possible breakout.
                derm.breakout()
                #Raise the possibility of a free product.
                derm.voucher()

        #If they asked for mandelic acid:
        elif payment == "mandelic":
            print("You bought a bottle of lactic acid for $25! This will help your skin's acne, glow, wrinkles, and texture!\n")
            #Check that they have enough money.
            if derm.get_money() >= 25:
                #Remove $25 from one's money.
                derm.set_money(25)
                #Increase one's acne, glow, wrinkles, and texture stats.
                derm.set_acne()
                derm.set_glow()
                derm.set_wrinkles()
                derm.set_texture()
                #Trigger a possible breakout.
                derm.breakout()
                #Raise the possibility of a free product.
                derm.voucher()

        #If they asked for azelaic acid:
        elif payment == "azelaic":
            print("You bought a bottle of azealic acid for $22! This will help your skin's acne, glow, and texture!\n")
            #Check that they have enough money.
            if derm.get_money() >= 22:
                #Remove $22 from one's money.
                derm.set_money(22)
                #Increase one's acne, glow, and texture stats.
                derm.set_acne()
                derm.set_glow()
                derm.set_texture()
                #Trigger a possible breakout.
                derm.breakout()
                #Raise the possibility of a free product.
                derm.voucher()
            
        #If they asked for ferulic acid:
        elif payment == "ferulic":
            print("You bought a bottle of ferulic acid for $21! This will help your skin's glow and wrinkles!\n")
            #Check that they have enough money.
            if derm.get_money() >= 21:
                #Remove $21 from one's money.
                derm.set_money(21)
                #Increase one's glow and wrinkles stats.
                derm.set_glow()
                derm.set_wrinkles()
                #Trigger a possible breakout.
                derm.breakout()
                #Raise the possibility of a free product.
                derm.voucher()

        #If they asked for kojic acid:
        elif payment == "kojic":
            print("You bought a bottle of kojic acid for $29! This will help your skin's acne and glow!\n")
            #Check that they have enough money.
            if derm.get_money() >= 29:
                #Remove $29 from one's money.
                derm.set_money(29)
                #Increase one's acne and glow stats.
                derm.set_acne()
                derm.set_glow()
                #Trigger a possible breakout.
                derm.breakout()
                #Raise the possibility of a free product.
                derm.voucher()

        #If they asked for ascorbic acid:
        elif payment == "ascorbic":
            print("You bought a bottle of L-ascorbic acid for $26! This will help your skin's glow, hydration, and wrinkles!\n")
            if derm.get_money() >= 26:
                #Remove $29 from one's money.
                derm.set_money(26)
                #Increase one's glow, hydration, and wrinkles stats.
                derm.set_glow()
                derm.set_hydration()
                derm.set_wrinkles()
                #Trigger a possible breakout.
                derm.breakout()
                #Raise the possibility of a free product.
                derm.voucher()

        #If the input provided doesn't refer to any of the above skincare acids:
        else:
            print("Please choose an available skincare product.\n")

    #If one has run out of money:
    if derm.get_money() <= 19:
        print(f"You do not have enough money to buy anything else! Regardless, your progress in taking care of yourself a {derm.progress} out of 10!")

    #If one has maxed out all five stats:
    if derm.get_acne() + derm.get_glow() + derm.get_hydration() + derm.get_wrinkles() + derm.get_texture() == 50:
        print(f"Congratulations! You have improved your skin for the better, and with ${derm.get_money()} left in the bank!")
        
if __name__ == "__main__":
    main()