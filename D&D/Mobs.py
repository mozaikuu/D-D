from Healthbars import *

class Mob:
  def __init__(self):
    self.hp = 1
    self.dmg = 1
    self.hp_color = "red"
    self.healthbar = HealthBar(self, color = self.hp_color)

class Bandit(Mob):
  weapon = "sword"

class goblin(Mob):
  weapon = "dagger"

class hobogoblin(goblin):
  weapon = "club"

class wolf(Mob):
  def bite():
    pass

class lich(Mob):
  pass

class dragon(Mob):
  pass

class troll(Mob):
  pass

class fishcat(Mob):
  pass

class golem(Mob):
  pass

class timegod(Mob):
  pass

class angel(Mob):
  pass

class demon(Mob):
  pass



