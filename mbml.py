#build in a quit flag

 
import time
import os

#imported file for text screen
# title screen
print("\n==================================================================")
print("¤¸¸.•´¯`•¸¸.•..>> Michael Bay Mad Lib Generator <<...•.¸¸•´¯`•.¸¸¤")
print("==================================================================\n")
print('"Some nights I sleep like a baby. Other nights its, Oh God, I\njust came up with a bomb shot." - Michael Bay\n')
print("------------------------------------------------------------------\n\n")
print("To get started with your Michael Bay Mad Lib, type START:\n>")


def start_madlib():
# Prompts user to begin or quit  
    begin = input(">").lower()

    if begin == "start":
        print("1)Put your CAP LOCK on NOW\n")
        time.sleep(2)
        print("2)Buckle up! It's going to be a slow-motion, rotating, exploding, shit show...\n")
        time.sleep(2)
        print("3)Please be patient with the questions -- it will be worth it in the end!)\n")
        time.sleep(2)
        print("..........")
        time.sleep(5)
        os.system('clear')

    if begin == "quit":
        print("Fine. See ya.")

# If user types something other than start or quit 
    elif begin != "start":
        print("Please type START\n")
        return start_madlib()
    

start_madlib()

def play_again():
# Asks user if wants to restart
    playagain = input("\nYou're hilarious! Would you like to play again?\n>").lower()

    if playagain.startswith("y"):
        return ask_inputs()

    else:
        print("\nThis was fun! See ya later.")

def ask_inputs():

#lots of repetition here -- find more efficient way?

    mans_name = input("Enter a man's name:\n>").upper()

    occupation = input("\nEnter an occupation:\n>").upper()

    noun = input("\nEnter a noun:\n>").upper()

    noun2 = input("\nEnter a noun:\n>").upper()

    noun3 = input("\nEnter a noun:\n>").upper()

    shape = input("\nEnter a shape:\n>").upper()

    man2_name = input("\nEnter a man's name:\n>").upper()

    verb = input("\nEnter a verb:\n>").upper()

    wom_name = input("\nEnter a woman's name:\n>").upper()

    bodypart = input("\nEnter a body part:\n>").upper()

    verb2 = input("\nEnter a verb:\n>").upper()

    noun4 = input("\nEnter a noun:\n>").upper()

    noun5 = input("\nEnter a noun:\n>").upper()

    histdoc = input("\nEnter a historic document:\n>")

    verb3 = input("\nEnter a verb:\n>").upper()

    noun6 = input("\nEnter a noun:\n>").upper()

    noun7 = input("\nEnter a noun:\n>").upper()

    noun8 = input("\nEnter a noun:\n>").upper()

    verb4 = input("\nEnter a verb:\n>").upper()

    noun9 = input("\nEnter a noun:\n>").upper()

    adjective = input("\nEnter an adjective:\n>").upper()

    adjective2 = input("\nEnter an adjective:\n>").upper()

    emotion = input("\nEnter an emotion:\n>").upper()

    verb5 = input("\nEnter a verb:\n>").upper()

    noun10 = input("\nEnter a noun:\n>").upper()

    noun11 = input("\nEnter a noun:\n>").upper()

    verb6 = input("\nEnter a verb:\n>").upper()


    print("\nThe moment you've been waiting for!......\n")
    
    time.sleep(2) 
    os.system('clear')

    # create print mad lib function

    print("******************************************************************************\n")
    print("Coming soon to a theater near you, Michael Bay directs the movie of the summer...\n")
    print(f"{mans_name} is a normal {occupation}. Then, one day, {noun} explodes, causing\n a {noun2} to blow up, and a nearby {noun3} erupts into a {shape} of flames.\n {man2_name} realizes he's being chased by the government, who's trying to {verb} him.\n")

    print(f"While on the run, he teams up with an incredibly attractive woman, who has an\n incredible {wom_name}. She may be from the streets, but she can {bodypart} like nobodys business.\n")
    print(f"The duo decide to turn the tables on their pursurers by blowing up a {verb2},\n which triggers a chain reaction, causing the local {noun4}, {noun5} and the {histdoc} to explode.\n")
    print(f"Then, the bad guy's helicopter gets {verb3} by a piece of {noun6}, from which\n the {noun7} exploded, and the helicopter explodes and falls onto a {noun8}, \ncausing it to {verb4}, which shoots a fireball straight into the \nheart of {noun9} and destroys the bad guy leader.\n")
    print(f"Everything is {adjective} and the two decide that such a {adjective2} ordeal\n has caused them to fall in {emotion} with each other. They decide to celebrate by {verb5}ing on the {noun10}, \nand they even managed to use a {noun11} from the beginning of the movie \nto {verb6} the whole story together.\n") 

    print("\n*****************************************************************************\n")

    return play_again()



ask_inputs()




    


