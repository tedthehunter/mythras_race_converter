import itertools

def possible_combinations(*lists):
    results = []
    for i in itertools.product(*lists):
        results.append(sum(i))
    print(results)
        
test1 = [i for i in range(6)]
test2 = [i for i in range(6)]
test3 = [i for i in range(6)]

test4 = [test1, test2, test3]
  
possible_combinations(test4)