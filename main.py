import itertools
import matplotlib.pyplot as plt

class PolyDie:
    def __init__(self, sides):
        self.sides = sides
        self.name = f'd{self.sides}'
        self.avg = (1+self.sides)/2
        
    def __repr__(self):
        return f'{self.name} object'
    
    def get_all_results(self):
        self.results = [i for i in range(self.sides)]
        return self.results
    
    
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
        self.range = range(self.min_score, self.max_score)
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
        
    def increment_bonus(self):
        die_sides = self.dice[0].sides
        num_of_dice = len(self.dice)
        self.bonus += 1
        self.initialize_dice(die_sides, num_of_dice)
        
    def decrement_bonus(self):
        die_sides = self.dice[0].sides
        num_of_dice = len(self.dice)
        self.bonus -= 1
        self.initialize_dice(die_sides, num_of_dice)
    
    def total_outcome_distribution(self):
        outcome_distribution = [0 for i in range(len(self.dice), (len(self.dice) * self.dice[0].sides) + 1)]
        individual_outcomes = [die.get_all_results() for die in self.dice]
        for i in itertools.product(*individual_outcomes):
            outcome_distribution[sum(i)] += 1
        outcome_distribution_percentage = [round((num/sum(outcome_distribution) * 100), 2) for num in outcome_distribution]
        return outcome_distribution_percentage
    
    def display_characteristic_distribution(self):
        x_ticks = [i for i in range(self.min_score, self.max_score + 1)]
        x_labels = [str(num) for num in x_ticks]
        
        y_data = self.total_outcome_distribution()
        y_ticks = [num for num in y_data]
        y_labels = [f'{num}%' for num in y_data]
        
        plt.bar(x_ticks, y_data)
        
        plt.title(f'{self.name} Roll Distribution')
        plt.xlabel('Possible Roll Results')
        plt.ylabel('Probability')
        
        plt.xticks(x_ticks, x_labels)
        plt.yticks(y_ticks, y_labels)
        
        plt.show()
    
    
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
    
    def display_all_characteristic_distribution(self):
        strength = self.strength.total_outcome_distribution()
        dexterity = self.dexterity.total_outcome_distribution()
        constitution = self.constitution.total_outcome_distribution()
        size = self.size.total_outcome_distribution()
        intelligence = self.intelligence.total_outcome_distribution()
        wisdom = self.wisdom.total_outcome_distribution()
        charisma = self.charisma.total_outcome_distribution()
        power = self.power.total_outcome_distribution()
        
        x_ticks = [i for i in range(3, 18)]
        x_labels = [str(num) for num in x_ticks]
        
        plt.bar(list(self.strength.range), strength, width=0.4, label = 'Strength')
        plt.bar(list(self.dexterity.range), dexterity, width=0.4, label = 'Dexterity')
        # plt.bar(x_ticks, intelligence, width=0.4, label='Intelligence')
        
        plt.legend()
        
        plt.show()
        

test = RacialProfile()

test.display_all_characteristic_distribution()