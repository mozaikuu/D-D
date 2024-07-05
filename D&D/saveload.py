import pickle

class saveload:
  def __init__(self):
    self.file_ext = ".save"
    
  def savestate(self, obj):
    with open(f"{obj.name}{self.file_ext}", "wb") as f:
      pickle.dump(obj, f)
    
  def loadstate(self, obj):
    with open(f"{obj.name}{self.file_ext}", "rb") as f:
      return pickle.load(f)
    
