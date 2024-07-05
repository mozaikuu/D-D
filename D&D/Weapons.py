class weapons:
  def __init__(self, name, weight, damage_types, damage, description, value):
    self.name = name
    self.weight = weight
    self.damage_types = damage_types
    self.damage = damage
    self.description = description
    self.value = value
    

class sword(weapons):
  pass

class bow(weapons):
  arrows = 30
  
  def shoot_bow(self):
    print("shooting bow")
    if self.arrows > 0:
      print("arrow shot")
      self.arrows -= 1
      return self.arrows
    else:
      print("you have no arrows")
      return self.arrows
    

class shield(weapons):
  pass

class wand(weapons):
  pass

class staff(weapons):
  pass

class axe(weapons):
    def throw_axe(self, enemy):
      print("throwing axe")

class dagger(weapons):
  pass

axe = axe("axe", 1, "slash", 4, "a normal axe", 1)
bow = bow("bow", 1, "pierce", 4, "a normal bow", 1)







class items: pass
class spells: pass