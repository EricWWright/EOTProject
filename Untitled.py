# EricWWright
# 3/19

###########################################################################################################
# Imports
from tkinter import *
from random import *

###########################################################################################################
# Global Vars
inventory = []

###########################################################################################################
# class Character():

#     def __init__(self, health):
#         self.health = health

# class Player(Character):

#     def __init__(self, defense, health=100):
#         super().__init__(health)
#         self.defense = defense

# class Monster(Character):

#     def __init__(self, name, strength, defense, health):
#         super().__init__(health)
#         self.name = name
#         self.strength = strength
#         self.defense = defense

class Application(Frame):
    """ GUI game where you fight monsters. """

    def __init__(self, master):
        """ Initialize the frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widget()
        self.displayText = ""
        self.mHealth = randrange(30, 100)
        self.mArmor = 0
        self.mDamage = randrange(0, 25)

    def create_widget(self):
        self.textOut = Text(self)
        self.textOut["bg"] = "black"
        self.textOut["fg"] = "white"
        self.textOut["bd"] = "50"
        self.textOut["padx"] = "10"
        self.textOut.grid(row=0, column=0, columnspan=6, sticky=NSEW)

        self.bttnAttack = Button(self)
        self.bttnAttack["text"] = "Attack"
        self.bttnAttack["command"] = self.attack
        self.bttnAttack.grid(row=1, column=1, columnspan=2, sticky=NSEW)

        self.bttnBlock = Button(self)
        self.bttnBlock["text"] = "Defend"
        self.bttnBlock["command"] = self.defend
        self.bttnBlock.grid(row=1, column=3, columnspan=2, sticky=NSEW)

        self.bttnItem = Button(self)
        self.bttnItem["text"] = "Item"
        self.bttnItem["command"] = self.item
        self.bttnItem.grid(row=2, column=3, columnspan=2, sticky=NSEW)

        self.bttnRun = Button(self)
        self.bttnRun["text"] = "Run"
        self.bttnRun["command"] = self.run
        self.bttnRun.grid(row=2, column=1, columnspan=2, sticky=NSEW)

        self.bttnMonster = Button(self)
        self.bttnMonster["text"] = "New Monster"
        self.bttnMonster["command"] = self.monster
        self.bttnMonster.grid(row=4, column=1, columnspan=2, sticky=NSEW)

    def attack(self):
        pDamage = randrange(5, 30)
        """ Attacks the monster and subtracts monter health. """
        if pDamage >= (self.mHealth + self.mArmor):
            dropItems = ("HP-potion", "DEF-potion", "ATK-potion")
            invetory.append(random.choice(dropItems))
            self.mHealth = 0
            self.displayText += "\nYou have slain the monster\nThe monster has droped an item\nThe item has been added to your inventory"
            self.textOut.delete(0.0, END)
            self.textOut.insert(0.0, self.displayText)
        elif pDamage < (self.mHealth + self.mArmor):
            self.mHealth = (self.mHealth + self.mArmor) - pDamage
            self.displayText += "\nThe monster takes: " + \
                str(pDamage) + " damage" + \
                "\nThe monster now has: " + \
                str(self.mHealth) + " health\n"
            self.textOut.delete(0.0, END)
            self.textOut.insert(0.0, self.displayText)

    def defend(self):
        """ Reduces damage from monster. """

    
    def item(self):
        """ Lets the user check their inventory and use items. """
        self.displayText += "\n" + str(inventory) + "\n"
        self.textOut.delete(0.0, END)
        self.textOut.insert(0.0, self.displayText)

    def run(self):
        """ User runs away from the monster. """
        self.displayText += "\nYou decide to run for your life\n"
        self.textOut.delete(0.0, END)
        self.textOut.insert(0.0, self.displayText)
    
    def monster(self):
        """ Creates new monster """
        self.displayText += "\nA new monster has appeared\n"
        self.textOut.delete(0.0, END)
        self.textOut.insert(0.0, self.displayText)
        self.mHealth = randrange(50, 100)
        self.mArmor = 15
        self.mDamage = randrange(5, 25)

# user = Player(0)
root = Tk()
root.title("Monster Fighter")
root.geometry("760x800")
app = Application(root)
root.mainloop()
