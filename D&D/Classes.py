from Healthbars import *
from Weapons import *
from Inventory import *

### Main Classes

class player:
  def __init__(self):
    self.name = ""
    self.gender = ""
    self.race = ""
    self.level = 1
    self.dmg_modifier = 1
    self.health_max = 10
    self.health = 10
    self.armor = 1
    self.spells = [] 
    self.bag = bag
    self.hp_color = "green"
    self.healthbar = HealthBar(self, color = self.hp_color)
    
  # def __init__(self):

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
  def hp(self):
    self.healthbar.update()
    self.healthbar.draw()
  
  
  
class bandit(player):
  def __init__(self, name, gender, race):
    super().__init__()
    self.name = name
    self.gender = gender
    self.race = race
    self.class_name = "bandit"

  
  def stab(self, enemy):
    pass
  
  def throw_rock(self, enemy):
    pass


class archer(player): #FIXME: Add bow to inventory
  def __init__(self, name, gender, race):
    super().__init__()
    self.name = name
    self.gender = gender
    self.race = race
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
  def __init__(self, name, gender, race):
    super().__init__()
    self.name = name
    self.gender = gender
    self.race = race
    self.class_name = "bruiser"
    self.race = race
  
  def engage(self, enemy):
    pass
  
  def hold_ground(self, enemy):
    pass
  
  


class wizard(player):
  def __init__(self, name, gender, race):
    super().__init__()
    self.name = name
    self.gender = gender
    self.race = race
    self.class_name = "wizard"
    self.race = race
  
  def stab(self, enemy):
    pass
  
  def throw_rock(self, enemy):
    pass
  


class tamer(player):
  def __init__(self, name, gender, race):
    super().__init__()
    self.name = name
    self.gender = gender
    self.race = race
    self.class_name = "tamer"
    self.race = race
  
  def stab(self, enemy):
    pass
  
  def throw_rock(self, enemy):
    pass
  


class tank(player):
  def __init__(self, name, gender, race):
    super().__init__()
    self.name = name
    self.gender = gender
    self.race = race
    self.class_name = "tank"
    self.race = race
  
  def stab(self, enemy):
    pass
  
  def throw_rock(self, enemy):
    pass
  


class bard(player):
  def __init__(self, name, gender, race):
    super().__init__()
    self.name = name
    self.gender = gender
    self.race = race
    self.class_name = "bard"
    self.race = race
  
  def stab(self, enemy):
    pass
  
  def throw_rock(self, enemy):
    pass
  

# if you do a certain action you instantly promote to a hidden class
  

class necromancer(player):
  def __init__(self, name, gender, race):
    super().__init__()
    self.name = name
    self.gender = gender
    self.race = race
    self.class_name = "hidden"
    self.hp_color = "purple"
    self.healthbar = HealthBar(self, color = self.hp_color)
  
  def stab(self, enemy):
    pass
  
  def throw_rock(self, enemy):
    pass

class blacksmith(player):
  def __init__(self, name, gender, race):
    super().__init__()
    self.name = name
    self.gender = gender
    self.race = race
    self.class_name = "hidden"
    self.hp_color = "purple"
    self.healthbar = HealthBar(self, color = self.hp_color)
  
  def stab(self, enemy):
    pass
  
  def throw_rock(self, enemy):
    pass


  
class slave_owner(player):
  def __init__(self, name, gender, race):
    super().__init__()
    self.name = name
    self.gender = gender
    self.race = race
    self.class_name = "hidden"
    self.hp_color = "purple"
    self.healthbar = HealthBar(self, color = self.hp_color)
  
  def stab(self, enemy):
    pass
  
  def throw_rock(self, enemy):
    pass



# to fix it i think i migrate everything to this class
class MultiClass(necromancer, blacksmith, slave_owner):
  def __init__(self, name, gender, race):
    super().__init__(name, gender, race)
    self.name = name
    self.gender = gender
    self.race = race
    self.class_name = {"hidden" : necromancer, "hidden" : blacksmith, "hidden" : slave_owner}
    self.hp_color = "yellow"
    self.healthbar = HealthBar(self, color = self.hp_color)



### Sub Classes