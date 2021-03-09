items = [
         ['bread', 'milk'],
         ['bread', 'diaper', 'beer', 'eggs'],
         ['milk', 'diaper', 'beer', 'coke'],
         ['bread', 'milk', 'diaper', 'beer'],
         ['bread', 'milk', 'diaper', 'coke']
]
import itertools
from FPTree import FPTree

def find_frequent_patterns(transactions, support_threshold):
    tree = FPTree(transactions, support_threshold, None, None)
    return tree.mine_patterns(support_threshold)

def generate_association_rules(patterns, confidence_threshold):
    rules = {}

    for itemset in patterns.keys():
        upper_support = patterns[itemset]

        for i in range(1, len(itemset)):
            for antecedent in itertools.combinations(itemset, i):
                antecedent = tuple(sorted(antecedent))
                consequent = tuple(sorted(set(itemset) - set(antecedent)))

                if antecedent in patterns:
                    lower_support = patterns[antecedent]
                    confidence = float(upper_support) / lower_support

                    if confidence >= confidence_threshold:
                        rules[antecedent] = (consequent, confidence)

    return rules


def fPGrowthAlgo(transactions, support_threshold, confidence_threshold):
    patterns = find_frequent_patterns(transactions, support_threshold)
    print('Patterns :')
    print(patterns)
    
    frequent_set = generate_association_rules(patterns, confidence_threshold)
    print('Association Rules: ')
    print(frequent_set)

fPGrowthAlgo(items, 0.4, 0.6)
    