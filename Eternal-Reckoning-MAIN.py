import time
import random

#This is the main section, where we will do our main work. If you can, please describe what the sections you develop do. 

#This section is devoted to setting up the functions. Type in whatever functions you are going to use here.
#def Intro(): PLACEHOLDER()
    
def Mainmenu1():
    print("Welcome to Eternal Reckoning, young traveler. An exciting adventure awaits you.")
    time.sleep(5)
    Mainmenu2()
def Mainmenu2():
    print("""MENU:
    1. New Game
    2. Options
    3. Exit""")
    options = input("")
    if options == '1':
        print("""Very well, traveler. 
        Be warned, this journey is frought with danger. 
        You must defend yourself at some points, but I have confidence that you can handle yourself in a fight.
        Good luck, and may the gods watch over your battles.""")
        time.sleep(8)
        Intro()
    elif options == '2':
        print("So sorry, but the options tab is not available -I.E. this is just for looks-")
        time.sleep(4)
        return options
    elif options == '3':
        print("I see. You have not prepared yourself yet. Come back when you are ready")
        time.sleep(4.5)
        return
def Intro():
    print("In the beginning...")
    time.sleep(2)
    print("...since time immemorial...")
    time.sleep(2.5)
    print("""...There has been a myth of a man who conquered all,
    one who braved the toughest of lands,
    the harshest of seas,
    the deadliest of foes,
    to become the One True King of Lux.
    His name is unimportant,
    lost to the ever-changing sea of history,
    But he is known to the rest of the world...
    AND HIS NAME IS JOHN CENA@!!!!#@#E#YOLOSWAG420BLAZEIT""")
Mainmenu1()
