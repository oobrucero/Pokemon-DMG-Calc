from Classes import Multiplication
from Classes import Stats
from Classes import statStages
Mults = Multiplication
Stats1 = Stats
Stages = statStages
enemy_type1 = input("Enter the first type of the enemy: ").lower()
enemy_type2= input("Enter the 2nd type, none if monotype: ").lower()
your_type1 = input("Enter the first type of your pokemon").lower()
your_type2 = input("Enter the second type, none if monotype").lower()
move_type = input("Enter th type of your move").lower()
move_power = float(input("Enter the power of your move").lower())
move_atk = input("Is the move special or physical").lower()
weather = input("Enter the weather of the battle").lower()
Stats.your_level = float(input("Enter your level"))
Stats.your_attack = float(input("Enter your attack"))
Stats.your_sp_attack = float(input("Enter your special attack"))
Stats.their_defense = float(input("Enter their defense"))
Stats.their_special_defense = float(input("Enter their special defense"))
Stages.atk_stage = float(input("Enter your attack stage"))
Stages.spatk_stage = float(input("Enter your special attack stage"))
Stages.def_stage = float(input("Enter their defense stage"))
Stages.spdef_stage = float(input("Enter their special defense stage"))

normal_effective = {
   "normal": 0,
   "fire": 0,
   "water": 0,
   "grass": 0,
   "electric": 0,
   "ice" : 0,
   "fighting": 0,
   "poison": 0,
   "ground": 0,
   "flying": 0,
   "psychic": 0,
   "bug": 0,
   "rock": -1,
   "ghost": -4,
   "dragon": 0,
   "dark": 0,
   "steel": -1,
   "fairy": 0,
   "none" : 0,
}

fire_effective = {
   "normal": 0,
   "fire": -1,
   "water": -1,
   "grass": 1,
   "electric": 0,
   "ice" : 1,
   "fighting": 0,
   "poison": 0,
   "ground": 0,
   "flying": 0,
   "psychic": 0,
   "bug": 1,
   "rock": -1,
   "ghost": 0,
   "dragon": -1,
   "dark": 0,
   "steel": 1,
   "fairy": 0,
   "none" : 0,
}

water_effective = {
   "normal": 0,
   "fire": 1,
   "water": -1,
   "grass": -1,
   "electric": 0,
   "ice" : 0,
   "fighting": 0,
   "poison": 0,
   "ground": 1,
   "flying": 0,
   "psychic": 0,
   "bug": 0,
   "rock": 1,
   "ghost": 0,
   "dragon": -1,
   "dark": 0,
   "steel": 0,
   "fairy": 0,
   "none" : 0,
}

grass_effective = {
   "normal": 0,
   "fire": -1,
   "water": 1,
   "grass": -1,
   "electric": 0,
   "ice" : 0,
   "fighting": 0,
   "poison": -1,
   "ground": 1,
   "flying": -1,
   "psychic": 0,
   "bug": -1,
   "rock": 1,
   "ghost": 0,
   "dragon": -1,
   "dark": 0,
   "steel": -1,
   "fairy": 0,
   "none" : 0,
}

electric_effective = {
   "normal": 0,
   "fire": 0,
   "water": 1,
   "grass": -1,
   "electric": -1,
   "ice" : 0,
   "fighting": 0,
   "poison": 0,
   "ground": -4,
   "flying": 1,
   "psychic": 0,
   "bug": 0,
   "rock": 0,
   "ghost": 0,
   "dragon": -1,
   "dark": 0,
   "steel": 0,
   "fairy": 0,
   "none" : 0,
}

ice_effective = {
   "normal": 0,
   "fire": -1,
   "water": -1,
   "grass": 1,
   "electric": 0,
   "ice" : 0,
   "fighting": 0,
   "poison": 0,
   "ground": 1,
   "flying": 1,
   "psychic": 0,
   "bug": 0,
   "rock": 0,
   "ghost": 0,
   "dragon": 1,
   "dark": 0,
   "steel": -1,
   "fairy": 0,
   "none" : 0,
}

fighting_effective = {
   "normal": 1,
   "fire": 0,
   "water": 0,
   "grass": 0,
   "electric": 0,
   "ice" : 1,
   "fighting": 0,
   "poison": -1,
   "ground": 0,
   "flying": -1,
   "psychic": -1,
   "bug": -1,
   "rock": 1,
   "ghost": -4,
   "dragon": 0,
   "dark": 1,
   "steel": 1,
   "fairy": 0,
   "none" : 0,
}

poison_effective = {
   "normal": 0,
   "fire": 0,
   "water": 0,
   "grass": 1,
   "electric": 0,
   "ice" : 0,
   "fighting": 0,
   "poison": -1,
   "ground": -1,
   "flying": 0,
   "psychic": 0,
   "bug": 0,
   "rock": -1,
   "ghost": -1,
   "dragon": 0,
   "dark": 0,
   "steel": -4,
   "fairy": 1,
   "none" : 0,
}

ground_effective = {
   "normal": 0,
   "fire": 1,
   "water": 0,
   "grass": -1,
   "electric": 1,
   "ice" : 0,
   "fighting": 0,
   "poison": 1,
   "ground": 0,
   "flying": -4,
   "psychic": 0,
   "bug": -1,
   "rock": 1,
   "ghost": 0,
   "dragon": 0,
   "dark": 0,
   "steel": 1,
   "fairy": 0,
   "none" : 0,
}

flying_effective = {
   "normal": 0,
   "fire": 0,
   "water": 0,
   "grass": 1,
   "electric": -1,
   "ice" : 0,
   "fighting": 1,
   "poison": 0,
   "ground": 0,
   "flying": 0,
   "psychic": 0,
   "bug": 1,
   "rock": -1,
   "ghost": 0,
   "dragon": 0,
   "dark": 0,
   "steel": -1,
   "fairy": 0,
   "none" : 0,
}

psychic_effective = {
   "normal": 0,
   "fire": 0,
   "water": 0,
   "grass": 0,
   "electric": 0,
   "ice" : 0,
   "fighting": 1,
   "poison": 1,
   "ground": 0,
   "flying": 0,
   "psychic": -1,
   "bug": 0,
   "rock": 0,
   "ghost": 0,
   "dragon": 0,
   "dark": -4,
   "steel": -1,
   "fairy": 0,
   "none" : 0,
}

bug_effective = {
   "normal": 0,
   "fire": -1,
   "water": 0,
   "grass": 1,
   "electric": 0,
   "ice" : 0,
   "fighting": -1,
   "poison": -1,
   "ground": 0,
   "flying": -1,
   "psychic": 1,
   "bug": 0,
   "rock": 0,
   "ghost": -1,
   "dragon": 0,
   "dark": 1,
   "steel": -1,
   "fairy": -1,
   "none" : 0,
}

rock_effective = {
   "normal": 0,
   "fire": 1,
   "water": 0,
   "grass": 0,
   "electric": 0,
   "ice" : 1,
   "fighting": -1,
   "poison": 0,
   "ground": -1,
   "flying": 1,
   "psychic": 0,
   "bug": 1,
   "rock": 0,
   "ghost": 0,
   "dragon": 0,
   "dark": 0,
   "steel": -1,
   "fairy": 0,
   "none" : 0,
}

ghost_effective = {
   "normal": -4,
   "fire": 0,
   "water": 0,
   "grass": 0,
   "electric": 0,
   "ice" : 0,
   "fighting": 0,
   "poison": 0,
   "ground": 0,
   "flying": 0,
   "psychic": 1,
   "bug": 0,
   "rock": 0,
   "ghost": 1,
   "dragon": 0,
   "dark":-1,
   "steel": 0,
   "fairy": 0,
   "none" : 0,
}

dragon_effective = {
   "normal": 0,
   "fire": 0,
   "water": 0,
   "grass": 0,
   "electric": 0,
   "ice" : 0,
   "fighting": 0,
   "poison": 0,
   "ground": 0,
   "flying": 0,
   "psychic": 0,
   "bug": 0,
   "rock": 0,
   "ghost": 0,
   "dragon": 1,
   "dark": 0,
   "steel": -1,
   "fairy": -4,
   "none" : 0,
}

dark_effective = {
   "normal": 0,
   "fire": 0,
   "water": 0,
   "grass": 0,
   "electric": 0,
   "ice" : 0,
   "fighting": -1,
   "poison": 0,
   "ground": 0,
   "flying": 0,
   "psychic": 1,
   "bug": 0,
   "rock": 0,
   "ghost": 1,
   "dragon": 0,
   "dark": -1,
   "steel": 0,
   "fairy": -1,
   "none" : 0,
}

steel_effective = {
   "normal": 0,
   "fire": -1,
   "water": -1,
   "grass": 0,
   "electric": -1,
   "ice" : 1,
   "fighting": 0,
   "poison": 0,
   "ground": 0,
   "flying": 0,
   "psychic": 0,
   "bug": 0,
   "rock": 1,
   "ghost": 0,
   "dragon": 0,
   "dark": 0,
   "steel": -1,
   "fairy": 1,
   "none" : 0,
}

fairy_effective = {
   "normal": 0,
   "fire": -1,
   "water": 0,
   "grass": 0,
   "electric": 0,
   "ice" : 0,
   "fighting": 1,
   "poison": -1,
   "ground": 0,
   "flying": 0,
   "psychic": 0,
   "bug": 0,
   "rock": 0,
   "ghost": 0,
   "dragon": 1,
   "dark": 1,
   "steel": -1,
   "fairy": 0,
   "none" : 0,
}

move_type_dict = {
   "normal": normal_effective,
   "fire" : fire_effective,
   "water": water_effective,
   "grass": grass_effective,
   "electric": electric_effective,
   "ice": ice_effective,
   "fighting": fighting_effective,
   "poison": poison_effective,
   "ground": ground_effective,
   "flying": flying_effective,
   "psychic": psychic_effective,
   "bug": bug_effective,
   "rock": rock_effective,
   "ghost": ghost_effective,
   "dragon": dragon_effective,
   "dark": dark_effective,
   "steel": steel_effective,
   "fairy": fairy_effective,
}


if Stages.atk_stage >= 0: #CALCULATES STAT BOOSTS
   Stats.your_attack = Stats.your_attack * ((Stages.atk_stage + 2) / 2)
else:
   Stats.your_attack = Stats.your_attack * (2/(abs(Stages.atk_stage) + 1))
if Stages.spatk_stage >= 0:  # CALCULATES STAT BOOSTS
   Stats.your_sp_attack = Stats.your_sp_attack * ((Stages.spatk_stage + 2) / 2)
else:
   Stats.your_sp_attack = Stats.your_sp_attack * (2 / (abs(Stages.spatk_stage) + 1))
if Stages.def_stage >= 0:  # CALCULATES STAT BOOSTS
   Stats.their_defense = Stats.their_defense * ((Stages.def_stage + 2) / 2)
else:
   Stats.their_defense = Stats.their_defense * (2 / (abs(Stages.def_stage) + 1))
if Stages.spdef_stage >= 0:  # CALCULATES STAT BOOSTS
   Stats.their_special_defense = Stats.their_special_defense * ((Stages.spdef_stage + 2) / 2)
else:
   Stats.their_special_defense = Stats.their_special_defense * (2 / (abs(Stages.spdef_stage) + 1))
if move_type == your_type1 or your_type2: #CALCULATES STAB
   Mults.stab = 1.5 #MAYBE ADD ABILITIES
if weather == "rain": #CALCULATES WEATHER
   if move_type == "fire":
       Mults.weather = .5
   if move_type == "water":
       Mults.weather = 1.5
if weather == "sun":
   if move_type == "fire":
       Mults.weather = 1.5
   if move_type == "water":
       Mults.weather = .5
else:
   Mults.weather = 1
used_dictionary = move_type_dict.get(move_type) #SUPER EFFECTIVE CALCULATOR
effectiveness = used_dictionary.get(enemy_type1) + used_dictionary.get(enemy_type2)
if effectiveness == 0:
   Mults.type = 1
elif effectiveness == 1:
   Mults.type = 2
elif effectiveness == 2:
   Mults.type = 4
elif effectiveness == -1:
   Mults.type = .5
elif effectiveness == -2:
   Mults.type = .25
else:
   Mults.type = 0


Modifier_High= Mults.weather * Mults.stab * Mults.type
Modifier_Low = Mults.weather * Mults.stab * Mults.type * .85
Crit_Modifier_high = Mults.weather * Mults.stab * Mults.type * 1.5
CritModifier_Low = Mults.weather * Mults.stab * Mults.type * 1.5 * .85
if move_atk == "physical":
   HighNormal = ((((((Stats.your_level * 2)/5) + 2) * move_power * (Stats.your_attack/Stats.their_defense))/50) + 2) * Modifier_High
   LowNormal = ((((((Stats.your_level * 2)/5) + 2) * move_power * (Stats.your_attack/Stats.their_defense))/50) + 2) * Modifier_Low
   LowCrit = ((((((Stats.your_level * 2)/5) + 2) * move_power * (Stats.your_attack/Stats.their_defense))/50) + 2) * CritModifier_Low
   HighCrit = ((((((Stats.your_level * 2)/5) + 2) * move_power * (Stats.your_attack/Stats.their_defense))/50) + 2) * Crit_Modifier_high
if move_atk == "special":
   HighNormal = ((((((Stats.your_level * 2)/5) + 2) * move_power * (Stats.your_sp_attack/Stats.their_special_defense))/50) + 2) * Modifier_High
   LowNormal = ((((((Stats.your_level * 2)/5) + 2) * move_power * (Stats.your_sp_attack/Stats.their_special_defense))/50) + 2) * Modifier_Low
   LowCrit = ((((((Stats.your_level * 2)/5) + 2) * move_power * (Stats.your_sp_attack/Stats.their_special_defense))/50) + 2) * CritModifier_Low
   HighCrit = ((((((Stats.your_level * 2)/5) + 2) * move_power * (Stats.your_sp_attack/Stats.their_special_defense))/50) + 2) * Crit_Modifier_high

print("The attack will do " + str(LowNormal) + " to " + str(HighNormal) + " if there is no critical hit")
print("The attack will do " + str(LowCrit) + " to " + str(HighCrit) + " if there is a critical hit")
