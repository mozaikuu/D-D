# TODO: add tkinter

from Mobs import *
from Classes import *
from Weapons import *
from Dice20 import roll20


choice = input("What would you like to do? ")

istrue = True

while istrue:
  if choice == "1":
    print("actions")
    # loads a character and lists their stats, items and possible moves
  elif choice == "2":
    print("make a character")
    # saves a new character in a csv and lists their stats and possible moves
    char_name = input("character name: ")
    char_class = input("character class: ")
    
    if char_class == "bandit":
      char_name = bandit(char_name)
    elif char_class == "archer":
      pass
    elif char_class == "bruiser":
      pass
    elif char_class == "wizard":
      pass
    elif char_class == "tamer":
      pass
    elif char_class == "tank":
      pass
    elif char_class == "bard":
      pass
    elif char_class == "hidden":
      pass

    
  elif choice == "3":
    print("make a mob")
    # loads a mob and lists their stats
  elif choice == "4":
    print(roll20())
    # rolls 20 and prints the result
  elif choice == "5":
    print("quit")
    isture = False
    # closes the program
  else:
    print("invalid input")
    # reruns the choice input