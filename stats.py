import random, itertools
from main import PolyDie, Characteristic, RacialProfile, test
from scratch import possible_combinations


    
def total_poss_outcomes():
    # makes a list with 0 for each possible outcome
    outcomes = [0 for i in range(len(dice), (len(dice) * dice[0].sides) + 1)]
    # then add each possible result of dice and increment its place in outcomes