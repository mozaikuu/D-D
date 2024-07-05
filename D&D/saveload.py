# import pickle

# class saveload:
#   def __init__(self):
#     self.file_ext = ".save"
    
#   def savestate(self, obj):
#     with open(f"{obj.name}{self.file_ext}", "wb") as f:
#       pickle.dump(obj, f)
    
#   def loadstate(self, obj):
#     with open(f"{obj.name}{self.file_ext}", "rb") as f:
#       return pickle.load(f)
    
# Load States with class saveload
# slm.loadstate(moussa)
# Save States
# slm.savestate(moussa)


# import pickle

# # At the start of your script, load the moussa object from the file
# with open('moussa.pkl', 'rb') as f:
#     moussa = pickle.load(f)

# # At the end of your script, save the moussa object to a file
# with open('moussa.pkl', 'wb') as f:
#     pickle.dump(moussa, f)


import os
import pickle
from Classes import *

# Create your characters
# # init Players
moussa = necromancer("moussa", "female", "skeleton")
saif = bandit("saif", "male", "human")
khalid = bandit("khalid", "male", "human")
omar = bandit("omar", "male", "human")
nour = bandit("nour", "male", "human")
waleed = bandit("waleed", "male", "human")
mohamed = bandit("mohamed", "male", "human")

# Put all characters in a dictionary
characters = {'moussa': moussa, 'saif': saif, 'khalid': khalid, 'omar': omar, 'nour': nour, 'waleed': waleed, 'mohamed': mohamed}

def loadstate():

# Check if the file exists
  if os.path.exists('characters.pkl'):
      # If the file exists, load the characters from the file
      with open('characters.pkl', 'rb') as f:
          characters = pickle.load(f)
          return characters
  else:
      characters = {'moussa': moussa, 'saif': saif, 'khalid': khalid, 'omar': omar, 'nour': nour, 'waleed': waleed, 'mohamed': mohamed}
  

# At the end of your script, save the characters to a file
def savestate():
  with open('characters.pkl', 'wb') as f:
    pickle.dump(characters, f)