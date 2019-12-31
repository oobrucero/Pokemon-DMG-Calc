class Multiplication:
   def __init__(self, type, stab, held_item, weather, ability, critical):
       self.type = type
       self.stab = stab
       self.held_item = held_item
       self.weather = weather
       self.ability = ability
       self.critical = critical

class Stats:
   def __init__(self, your_level, your_attack, your_sp_attack, their_defense, their_special_defense):
       self.your_level = your_level
       self.your_attack = your_attack
       self.your_sp_attack = your_sp_attack
       self.their_defense = their_defense
       self.their_special_defense = their_special_defense

class statStages:
   def __init__(self, atk_stage, def_stage, spatk_stage, spdef_stage):
       self.atk_stage = atk_stage
       self.def_stage = def_stage
       self.spatk_stage = spatk_stage
       self.spdef_stage = spdef_stage
