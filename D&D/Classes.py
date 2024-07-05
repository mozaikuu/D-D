from Weapons import *

### Main Classes

class player:
  def __init__(self):

    self.race = "human"
    self.class_name = "player"
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

  def seduce(self, enemy):
    pass
  
  def ask_a_question(self, enemy):
    pass
  
  def leave(self, enemy):
    pass
  
  def presuade(self, enemy):
    pass
  
  def attack(self, enemy):
    pass
  
  def defend(self, enemy):
    pass
  
  def punch(self, enemy):
    pass
  
  def kick(self, enemy):
    pass
  
  
  
class bandit(player):
  def __init__(self, race):
    super().__init__()
    self.class_name = "bandit"
    self.race = race
    self.inventory = [axe, axe]
  
  def stab(self, enemy):
    pass
  
  def throw_rock(self, enemy):
    pass


class archer(player):
  def __init__(self, race):
    super().__init__()
    self.class_name = "archer"
    self.race = race
    self.inventory = {"bow" : bow, "arrows" : bow.arrows}
  
  def shoot_arrow(self):
    bow.shoot_bow()
    self.inventory["arrows"] = bow.arrows
    return self.inventory
  
  def gain_distance(self, enemy):
    pass
  
  def backflip(self, enemy):
    pass
  


class bruiser(player):
  def __init__(self, race):
    super().__init__()
    self.class_name = "bandit"
    self.race = race
    self.inventory = [axe, axe]
  
  def engage(self, enemy):
    pass
  
  def hold_ground(self, enemy):
    pass
  
  


class wizard(player):
  def __init__(self, race):
    super().__init__()
    self.class_name = "bandit"
    self.race = race
    self.inventory = [axe, axe]
  
  def stab(self, enemy):
    pass
  
  def throw_rock(self, enemy):
    pass
  


class tamer(player):
  def __init__(self, race):
    super().__init__()
    self.class_name = "bandit"
    self.race = race
    self.inventory = [axe, axe]
  
  def stab(self, enemy):
    pass
  
  def throw_rock(self, enemy):
    pass
  


class tank(player):
  def __init__(self, race):
    super().__init__()
    self.class_name = "bandit"
    self.race = race
    self.inventory = [axe, axe]
  
  def stab(self, enemy):
    pass
  
  def throw_rock(self, enemy):
    pass
  


class bard(player):
  def __init__(self, race):
    super().__init__()
    self.class_name = "bandit"
    self.race = race
    self.inventory = [axe, axe]
  
  def stab(self, enemy):
    pass
  
  def throw_rock(self, enemy):
    pass
  

# if you do a certain action you instantly promote to a hidden class
class hidden(player):
  def __init__(self, race):
    super().__init__()
    self.class_name = "bandit"
    self.race = race
    self.inventory = [axe, axe]
  
  def stab(self, enemy):
    pass
  
  def throw_rock(self, enemy):
    pass
  






  





### Sub Classes