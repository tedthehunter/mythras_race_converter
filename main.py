

class PolyDie:
    def __init__(self, sides):
        self.sides = sides
        self.name = f'd{self.sides}'
        
    def __repr__(self):
        return f'{self.name} object'
    
class Characteristic:
    def __init__(self, name, bonus, *dice):
        self.name = name
        self.bonus = bonus
        self.dice = dice
        self.min_score = len(self.dice) + self.bonus
        self.max_score = (len(self.dice) * self.dice[0].sides) + self.bonus
        self.range = f'{self.min_score}-{self.max_score}'
    
    def __repr__(self):
        return f'{self.name} characteristic object'
    
class RacialProfile:
    def __init__(self, name='Human'):
        self.name = name


d2 = PolyDie(2)
d4 = PolyDie(4)
d6 = PolyDie(6)
d8 = PolyDie(8)
d10 = PolyDie(10)
d12 = PolyDie(12)
d20 = PolyDie(20)

strength = Characteristic('Strength', 6, d6, d6)
print(strength)
print(strength.dice)
print(strength.range)
print(strength.bonus)