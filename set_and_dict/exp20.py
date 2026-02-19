from collections import Counter
inv1 = {'apples': 10, 'bananas': 5, 'oranges': 8}
inv2 = {'apples': 5, 'grapes': 12, 'bananas': 2}
merged_inv = dict(Counter(inv1) + Counter(inv2))
print(merged_inv)