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


