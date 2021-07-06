import random
import time
cores = ["Ash Wand","Ivy Wand","Ivy Wand","Oak Wand","Willow Wand","Birch Wand","Reed Wand"]
helps =["Hermoine","Ron","Draco","Dudley"]
print("****----WELCOME TO HARRY POTTER'S WIZARD WORLD GAME----***** ")
print("--------------------------------------------------------------")

print("What is your first name?")
name = input(">>> ")

print("What is your last name?")
lastname = input(">>> ")


def welcome():
    print("--------------------------------------------------------------")
    print("To " + name + " " + lastname + ":")
    print("")
    print("-----We are pleased to inform you that you have been ----\n ---"
          "----accepted into Hogwarts School of Witchcraft and Wizardry.------")
    time.sleep(0.5)
    print("-----Please find enclosed a list of all necessary books and equipment.-----")
    time.sleep(0.5)
    print("------We await your acceptance owl no later than July 31.----")
    time.sleep(0.5)
    print("")
    print("-----------Term Begins on September the First.--------------")
    time.sleep(0.5)
    print("-----Take the train from Platform 9 3/4 at King's Cross Station.----")
    time.sleep(0.5)
    print("")
    print("-------Hogwarts School of Witchcraft and Wizardry----")
    time.sleep(0.5)
    print("")
    print("--------------------------------------------------------------")
    print("--------------------------------------------------------------")
    print("Do you accept? (y/n)")
    accept = input(">>> ").upper()
    if accept == "Y":
        Ollivanders()
    elif accept == "N":
        WowYouJustMissedAGreatChance()
    print("--------------------------------------------------------------")

def Ollivanders():  # wand

    print("You travel to Diagon Alley to do your school shopping.")
    print("Where do you get your wand?")
    print("")
    print("1. Delacour's")
    print("2. Gregorovich's Wands")
    print("3. Ollivanders: Makers of Fine Wands since 305 B.C.")
    print("")
    print("--------------------------------------------------------------")
    print("--------------------------------------------------------------")
    wandshop = input("1, 2, or 3? ")
    if wandshop == "1":
        print("----Delacour's isn't in village-----")
        print("*****choose again*******")
        Ollivanders()
    elif wandshop == "2":
        print("----His shop is closed----")
        print("********choose again********")
        Ollivanders()
    elif wandshop == "3":
        print("You're headed on the right track to be a great witch or wizard.")
        print("--------------------------------------------------------------")
        print("--------------------------------------------------------------")
        time.sleep(3)
        YourWand()
def YourWand():
    print("Welcome to Ollivander's!")
    print("")
    print("Are you most:")
    print("A. Kind and Generous")  # Ash
    print("B. Tenacious")  # Ivy
    print("C. A good leader")  # Holly
    print("D. Full of life")  # Birch
    print("E. Knowledgeable")  # Reed
    print("F. Strong and Flexible")  # Willow
    print("G. Confident and Optimistic")  # Oak
    print("")
    wood = input(">>> ").upper()
    print("--------------------------------------------------------------")
    print("--------------------------------------------------------------")
    core= random.choice(cores)
    print("")
    if wood == "A":
        print("You receive an ^^^^^ " + core)
        print("")
        print("**********Randomly***********")
        time.sleep(5)
        Platform934()
    elif wood == "B":
        print("You receive an ^^^^^ " + core )
        print("")
        print("**********Randomly***********")
        time.sleep(5)
        Platform934()
    elif wood == "C":
        print("You receive a ^^^^^^" + core )
        print("")
        print("**********Randomly***********")
        time.sleep(5)
        Platform934()
    elif wood == "D":
        print("You receive a  ^^^^^" + core )
        print("")
        print("**********Randomly***********")
        time.sleep(5)
        Platform934()
    elif wood == "E":
        print("You receive a  ^^^^^^^^" + core )
        print("")
        print("**********Randomly***********")
        time.sleep(5)
        Platform934()
    elif wood == "F":
        print("You receive a ^^^^^^^ "+core )
        print("")
        print("**********Randomly***********")
        time.sleep(5)
        Platform934()
    elif wood == "G":
        print("You receive an  ^^^^^^^^^"  + core)
        print("")
        print("**********Randomly***********")
        time.sleep(5)
        Platform934()
def Platform934():
	print("You need to get onto the platform. How do you get on?")
	print("")
	print("A. Stand between platforms nine and ten")
	print("B. Run at the barrier between platforms nine and ten")
	print("C. Fly a car to Hogwarts.")
	print("")
	platform = input(">>> ").upper()
	if platform == "A":
		print("Do you know anything about Harry Potter?")
		Platform934()
	elif platform == "B":
		print("You make it onto the platform and board the train.")
		time.sleep(5)
		Helping()
	elif platform == "C":
		print("Do you own a flying car?---- chose Again")
		Platform934()

def Helping():
    print("Now Hermoine and Ron are your friends at school")
    help =random.choice(helps)
    w=help
    print("")
    print("^^^"+help+"^^^^"+" Needs your help save your friend from woldmart")
    print("-------------------------------------")
    time.sleep(5)
    print("-----Choose a nor between(1-4) For partner----")
    print("--------------------------------------------------------------")
    H=input(">>").upper()
    if H=='1':
        Hermoine()
    elif H=='2':
        Ron()
    elif H=='3':
        Draco()
    elif H=='4':
        Dudley()
    else:
        woldmart()
def Hermoine():
    print("-------------------------------------")
    print(" You and hermoine are match for woldmart")
    time.sleep(3)
    poison()
    print("****THE POISON YOU PREPARED WAS STRONG ENOUGH TO KILL WOLDMART*****")
    print("you both killed woldmart")
    Win()
def Ron():
    print("-------------------------------------")
    time.sleep(3)
    print("You and Ron are match for woldmart")
    poison()
    print("****THE POISON YOU PREPARED WAS STRONG ENOUGH TO KILL WOLDMART*****")
    print("you both killed woldmart")
    Win()
def Draco():
    print("-------------------------------------")
    time.sleep(3)
    print("you both qurelled together")
    poison()
    print(" ")
    print("****THE POISON YOU PREPARED WAS NOT STRONG ENOUGH TO KILL WOLDMART*****")
    woldmart()
def Dudley():
    print("-------------------------------------")
    time.sleep(3)
    print("Dudley is lazy and careless")
    print("because of him you may loose")
    poison()
    print(" ")
    print("****THE POISON YOU PREPARED WAS NOT STRONG ENOUGH TO KILL WOLDMART*****")
    woldmart()
def woldmart():
    print("-------------------------------------")
    print("you are a coward")
    time.sleep(3)
    for i in range(1, 2 * 5):
        for j in range(1, 2 * 5):
            if i == j or i + j == 2 * 5:
                print('*', end='')
            else:
                print(' ', end='')
        print()
    print("woldmart killed you and your friend")
    print("------The end----------")

reci = {"fang": 6,
        "heat": 250,
        "slugs": 4,
        "quills": 2,
        "stirs": 5

        }
def poison():
    print("To kill wold mart you should prepare potion of posion")
    time.sleep(3)
    print("-----------------------------------------------------------------------------------------")
    recipe = """Cure for Boils:
	1. Add 6 snake fangs to the mortar.
	2. Crush into a fine powder using the pestle.
	3. Add 4 measures of the crushed fangs to your cauldron.
	4. Heat the mixture to 250 for 10 seconds.
	5. Wave your wand.
	6. Leave to brew and return in 33-45 minutes.
	7. Add 4 horned slugs to your cauldron.
	8. Take the cauldron off the fire before adding the next ingredient.
	10. Add 2 porcupine quills to your cauldron.
	11. Stir 5 times, clockwise.
	12. Wave your wand to complete the potion.

	 """
    print("-----------------------------------------------------------------------------------------")
    print(recipe)
    fangs = input("How many snake fangs do you put in? ")
    if fangs == "6":
        print("Good job!")
    else:
        print("Your potion already goes up in smoke. You restart, this time adding the correct number of fangs.")
        print(reci)
        print("________________Read the portion content_______________________")
    time.sleep(3)

    # print(recipe)
    heat = input("To what degree do you heat it to? ")
    if heat == "250":
        print("Good job!")
    else:
        print("Your potion now smells like rotten overcooked eggs.")
        print(reci)
        print("________________Read the portion content_______________________")
    time.sleep(3)

    # print(recipe)
    slugs = input("How many horned slugs do you put in? ")
    if slugs == "4":
        print("Good job!")
    else:
        print("Your potion is ruined. It bursts like the number of slugs you put in.")
        print(reci)
        print("________________Read the portion content_______________________")
    time.sleep(3)

    # print(recipe)
    quills = input("How many porcupine quills do you put in? ")
    if quills == "2":
        print("Good job!")
    else:
        print("You fail your first ever potions ")
        print(reci)
        print("________________Read the portion content_______________________")
        time.sleep(3)
    time.sleep(3)

    stirs = input("How many times do you stir? ")
    if stirs == "5":
        print("Good job!")
    else:
        print("You fail your first ever potions class.")
        print(reci)
        print("________________Read the portion content_______________________")
        time.sleep(3)
        woldmart()
    print("Great job! There is now pink smoke rising from your cauldron. You receive an E.")
    time.sleep(3)
def Win():
    print("$$$$$$____YOU WIN_____$$$$$$$$$")
    time.sleep(3)
    print("-------The end--------")
    S=input("play again yes or no Y/N ?")
    if S==S:
        welcome()
    else:
        exit()

def WowYouJustMissedAGreatChance():
	sure = input("Are you sure? y/n ")
	if sure == "n":
		Ollivanders()
	else:
		print("you missed great chance \n ------The end---------- ")
		exit()
welcome()
