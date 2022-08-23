import random, itertools
from main import PolyDie
from scratch import possible_combinations

# def roll_sample():
#     num_roll = 6000000

#     frequency = [0 for i in range(6)]

#     for roll in range(num_roll):
#         face = random.randrange(1, 7)
#         frequency[face - 1] += 1
        
#     print(f'Face{"Frequency":>13}')
#     for i, j in enumerate(frequency):
#         print(f'{i + 1:>4}{j:>13}')
    

def total_poss_outcomes(*dice):
    lists = [die.get_range() for die in dice]
    results = possible_combinations()
    
  
total_poss_outcomes(PolyDie(6), PolyDie(6), PolyDie(6))    
                           
                           
# x = [i for i in range(6)]
# y = [i for i in range(6)]
# z = [i for i in range(6)]
# print([i+j+k for i in x for j in y for k in z])