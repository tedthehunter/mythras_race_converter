

class PolyDie:
    def __init__(self, sides):
        self.sides = sides
        self.name = f'd{self.sides}'
        self.avg = (1+self.sides)/2
        
    def __repr__(self):
        return f'{self.name} object'
    
    
class Characteristic:
    def __init__(self, name, die_sides, num_of_dice, bonus=0):
        self.name = name
        self.bonus = bonus
        self.initialize_dice(die_sides, num_of_dice)
    
    def __repr__(self):
        return f'{self.name} characteristic object'
    
    def initialize_dice(self, die_sides, num_of_dice):
        self.dice = []
        for i in range(num_of_dice):
            self.dice.append(PolyDie(die_sides))
        self.min_score = num_of_dice + self.bonus
        self.max_score = (len(self.dice) * self.dice[0].sides) + self.bonus
        self.range = f'{self.min_score}-{self.max_score}'
        self.avg_score = self.dice[0].avg * num_of_dice
    
    def increment_num_of_dice(self):
        die_sides = self.dice[0].sides
        num_of_dice = len(self.dice) + 1
        self.initialize_dice(die_sides, num_of_dice)
        
    def decrement_num_of_dice(self):
        die_sides = self.dice[0].sides
        num_of_dice = len(self.dice)
        if num_of_dice > 1:
            num_of_dice -= 1
            self.initialize_dice(die_sides, num_of_dice)
        
    def increment_dice_size(self):
        die_sides = self.dice[0].sides
        num_of_dice = len(self.dice)
        if die_sides < 12:
            die_sides += 2
            self.initialize_dice(die_sides, num_of_dice)
        elif die_sides == 12:
            die_sides = 20
            self.initialize_dice(die_sides, num_of_dice)
        else:
            return f'Dice size at maximum!'
        
    def decrement_dice_size(self):
        die_sides = self.dice[0].sides
        num_of_dice = len(self.dice)
        if die_sides == 20:
            die_sides = 12
            self.initialize_dice(die_sides, num_of_dice)
        elif die_sides > 2:
            die_sides -= 2
            self.initialize_dice(die_sides, num_of_dice)
        else:
            return f'Dice size at minimum!'
        
    
    
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
        
    def __repr__(self):
        return f'{self.name} profile object'
        

test = RacialProfile()
print(test.strength.dice)
print(test.strength.avg_score)
test.strength.increment_num_of_dice()
print(test.strength.dice)
print(test.strength.avg_score)
test.strength.increment_dice_size()
print(test.strength.dice)
print(test.strength.avg_score)
test.strength.increment_num_of_dice()
print(test.strength.dice)
print(test.strength.avg_score)
test.strength.increment_dice_size()
print(test.strength.dice)
print(test.strength.avg_score)