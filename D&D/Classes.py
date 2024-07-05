### Main Classes

class player:
  def __init__(self):
    self.level = 1
    self.dmg_modifier = 1
    self.hp = 1
    self.armor = 1
    self.gold = 1
    self.mana = 1
    
    inventory = []
    
    # self.strength = 1
    # self.dexterity = 1
    # self.intelligence = 1
    # self.charisma = 1

  def threaten(self, enemy):
    pass
  
  def punch(self, enemy):
    pass
  
  def kick(self, enemy):
    pass
  
  
  
class bandit(player):
  
  def stab(self, enemy):
    pass
  
  def throw_rock(self, enemy):
    pass



class archer(player):
  
  def shoot_arrow(self, enemy):
    pass
  
  def gain_distance(self, enemy):
    pass
  
  def backflip(self, enemy):
    pass
  


class bruiser(player):
  
  def stab(self, enemy):
    pass
  
  def throw_rock(self, enemy):
    pass
  


class wizard(player):
  
  def stab(self, enemy):
    pass
  
  def throw_rock(self, enemy):
    pass
  


class tamer(player):
  
  def stab(self, enemy):
    pass
  
  def throw_rock(self, enemy):
    pass
  


class tank(player):
  
  def stab(self, enemy):
    pass
  
  def throw_rock(self, enemy):
    pass
  


class bard(player):
  
  def stab(self, enemy):
    pass
  
  def throw_rock(self, enemy):
    pass
  

# if you do a certain action you instantly promote to a hidden class
class hidden(player):
  
  def stab(self, enemy):
    pass
  
  def throw_rock(self, enemy):
    pass
  






  





### Sub Classes