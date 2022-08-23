import itertools

def possible_combinations(list_of_lists):
    results = []
    for i in itertools.product(*list_of_lists):
        results.append(sum(i))
    return results
        
test1 = [i for i in range(6)]
test2 = [i for i in range(6)]
test3 = [i for i in range(6)]

test4 = [test1, test2, test3]
  
# possible_combinations(test4)