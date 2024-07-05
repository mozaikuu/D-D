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
  pass

class shield(weapons):
  pass

class wand(weapons):
  pass

class staff(weapons):
  pass

class axe(weapons):
  pass

class dagger(weapons):
  pass

longsword = sword("longsword", 1, "slash", 4, "a normal longsword", 1)
