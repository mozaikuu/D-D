# TODO: add tkinter
# TODO: fix inventory better code? its kinda good ngl
# TODO: make better save load system later

import pickle
from Mobs import *
from Class import *
from Weapons import *
from Dice20 import *
from saveload import *

# save/load
# def loadstate(characters):
#   with open('characters.pkl', 'rb') as f:
#     characters = pickle.load(f)
#     return characters

# def savestate(characters):
#   with open('characters.pkl', 'wb') as f:
#     pickle.dump(characters, f)


#################################################################################
# Testing the code / Spotify cries in the wind



#access characters:
moussa = necromancer("moussa", "female", "skeleton")
heldback = bandit("heldback", "not specified", "orc")
professor_dragon = comedian("professor_dragon", "female", "kobold")
# omar = bandit("omar", "male", "human")
# nour = bandit("nour", "male", "human")
# waleed = bandit("waleed", "male", "human")
# mohamed = bandit("mohamed", "male", "human")

characters = {"moussa":[moussa], "khalid":[professor_dragon], "saif":[heldback]}

# mobs
guard = bandit("Guard", "male", "human")

# characters = {"moussa":[moussa], "saif":[saif], "khalid":[khalid], "omar":[omar], "nour":[nour], "waleed":[waleed], "mohamed":[mohamed]}

# initial
# savestate(characters)

# loadstate(characters)
print(characters)

# moussa= MultiClass("moussa", "female", "skeleton") # FIXME Multiclass
# -------------------------------------------------------------------------------






# Create your characters
# # init Players


# Put all characters in a dictionary



    
    

# moussa.bag.weapons.append("sword")
# moussa.bag.weapons.append(arrow)


# print(moussa.bag.weapons)
# print(moussa.__dict__)

# print(saif.bag.weapons)


# GAME
counter = 5

heldback.level = 5
print(heldback.__dict__)
professor_dragon.health = 10
professor_dragon.hp()
heldback.health = 9
heldback.hp()

# guard.hp()
# guard.hp()
# guard.hp()

heldback.bag.weapons.append("dagger") # FIXME += 10
heldback.bag.items.append("armor") # FIXME += 10
heldback.bag.items.append("another set of keys") # FIXME += 10
heldback.bag.gold = 0

professor_dragon.bag.weapons.append("sword") # FIXME += 10
professor_dragon.bag.items.append("cloth")
professor_dragon.bag.gold = 0

print(roll20())



# print(heldback.bag.gold)



# print(professor_dragon)


# moussa.health += 0
# saif.health += 0
# khalid.health += 0
# omar.health += 0
# nour.health += 0
# waleed.health += 0
# mohamed.health += 0

# saif.bag.gold += 0
# print(saif.bag.gold)




# moussa.hp()
# saif.hp()
# khalid.hp()
# omar.hp()
# nour.hp()
# waleed.hp()
# mohamed.hp()

# whenever i save it resets everything
# savestate(characters)
# -------------------------------------------------------------------------------

# # slm = saveload()

# # Load Players
# moussa = necromancer("moussa", "female", "skeleton")
# # saif = bandit("saif", "male", "human")
# # khalid
# # omar
# # nour
# # waleed
# # mohamed

# # At the start of your script, load the moussa object from the file
# with open('moussa.pkl', 'rb') as f:
#     moussa = pickle.load(f)
    





# moussa.bag.weapons.append("sword")
# moussa.bag.weapons.append(arrow)


# print(moussa.bag.weapons)
# print(moussa.__dict__)

# # moussa.health = 6

# moussa.healthbar.update()
# moussa.healthbar.draw()



# # At the end of your script, save the moussa object to a file
# with open('moussa.pkl', 'wb') as f:
#     pickle.dump(moussa, f)




#################################################################################

# save state



# istrue = False  #FIXME: Turn Back on

# while istrue:
#   choice = input("What would you like to do? ")
  
#   if choice == "1":
#     print("actions")
#     # loads a character and lists their stats, items and possible moves
#   elif choice == "2":
#     print("make a character")
#     # saves a new character in a csv and lists their stats and possible moves
#     char_name = input("character name: ")
#     char_class = input("character class: ")
    
#     if char_class == "bandit":
#       char_name = bandit(char_name)
#     elif char_class == "archer":
#       pass
#     elif char_class == "bruiser":
#       pass
#     elif char_class == "wizard":
#       pass
#     elif char_class == "tamer":
#       pass
#     elif char_class == "tank":
#       pass
#     elif char_class == "bard":
#       pass
#     elif char_class == "hidden":
#       pass

    
#   elif choice == "3":
#     print("make a mob")
#     # loads a mob and lists their stats
#   elif choice == "4":
#     print(roll20())
#     # rolls 20 and prints the result
#   elif choice == "5":
#     print("quit")
#     isture = False
#     # closes the program
#   else:
#     print("invalid input")
#     # reruns the choice input
    
    
    

