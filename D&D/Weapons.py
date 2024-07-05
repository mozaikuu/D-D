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
  def shoot_bow(self):
    pass
    
class arrows(weapons):
  count = 30
  pass

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


# arguments = (name, weight, damage_types, damage, description, value)
axe = axe("axe", 1, "slash", 4, "a normal axe", 1)
bow = bow("bow", 1, "pierce", 4, "a normal bow", 1)
arrow = arrows("arrow", 1, "pierce", 4, "a normal arrow", 1)







class items: pass
class spells: pass