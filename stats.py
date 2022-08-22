import random

num_roll = 6000000

frequency = [0 for i in range(6)]

for roll in range(num_roll):
    face = random.randrange(1, 7)
    frequency[face - 1] += 1
    
print(f'Face{"Frequency":>13}')
for i, j in enumerate(frequency):
    print(f'{i + 1:>4}{j:>13}')