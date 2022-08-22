

class PolyDie:
    def __init__(self, sides):
        self.sides = sides
        self.name = f'd{self.sides}'
        
    def __repr__(self):
        return f'{self.name} object'
    
class Characteristic:
    def __init__(self, name, die_sides, num_of_dice, bonus=0):
        self.name = name
        self.bonus = bonus
        self.dice = []
        for i in range(num_of_dice):
            self.dice.append(PolyDie(die_sides))
        self.min_score = num_of_dice + self.bonus
        self.max_score = (len(self.dice) * self.dice[0].sides) + self.bonus
        self.range = f'{self.min_score}-{self.max_score}'
    
    def __repr__(self):
        return f'{self.name} characteristic object'
    
class RacialProfile:
    def __init__(self, name='Human'):
        self.name = name
        self.strength = Characteristic('Strength', 6, 3)
        self.dexterity = Characteristic('Dexterity', 6, 3)
        self.constitution = Characteristic('Constitution', 6, 3)
        self.size = Characteristic('Size', 6, 2, 6)
        self.intelligence = Characteristic('Intelligence', 6, 2, 6)
        self.wisdom = Characteristic('Wisdom', 6, 3)
        self.charisma = Characteristic('Charisma', 6, 3)
        self.power = Characteristic('Power', 6, 3)
        



intelligence = Characteristic('Intelligence', 6, 2, 6)
print(intelligence)
print(intelligence.range)
print(intelligence.dice)
