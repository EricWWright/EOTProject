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
class Player():
    """ Creates player object and gives player attrbutes. """
    def __init__(self):
        self.pHealth = 100
        self.pArmor = 0
    
    def playerDamage(self):
        """ Calculates how much damage the player does to the monster. """
        pDamage = randrange(5, 30)
        return pDamage
    
class Monster():
    """ Creates monster object and gives monster attributes. """
    def __init__(self):
        self.mHealth = randrange(30, 100)
        self.mArmor = 0
    def monsterDamage(self):
        """ Calculates how much damage the monster does to the player. """
        mDamage = randrange(0, 25)
        return mDamage
    

class Application(Frame):
    """ GUI game where you fight monsters. """

    def __init__(self, master):
        """ Initialize the frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widget()

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
        self.bttnBlock["text"] = "Block"
        self.bttnBlock["command"] = self.block
        self.bttnBlock.grid(row=1, column=3, columnspan=2, sticky=NSEW)

        self.bttnItem = Button(self)
        self.bttnItem["text"] = "Item"
        self.bttnItem["command"] = self.item
        self.bttnItem.grid(row=2, column=3, columnspan=2, sticky=NSEW)

        self.bttnRun = Button(self)
        self.bttnRun["text"] = "Run"
        self.bttnRun["command"] = self.run
        self.bttnRun.grid(row=2, column=1, columnspan=2, sticky=NSEW)

    def attack(self):
        """ Attacks the monster and subtracts monter health. """
        if Player.playerDamage >= (Monster.mHealth + Monster.mArmor):
             print("The monster is dead")
             mHealth = 0
        elif pDamage < (mHealth + mArmor):
            print("The monster takes:", pDamage)
            mHealth = (mHealth + mArmor) - pDamage
            print("The monster now has:", mHealth, "health")

    def block(self):
        """ Reduces damage from monster. """

    
    def item(self):
        """ Lets the user check their inventory and use items. """

    def run(self):
        """ User runs away from the monster. """

root = Tk()
root.title("Monster Fighter")
root.geometry("760x800")
app = Application(root)
root.mainloop()
