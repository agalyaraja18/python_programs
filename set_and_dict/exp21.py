from collections import OrderedDict
my_list = list(input("Enter the list of items: ").split())
counts = {}
for item in my_list:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1
print(list(counts.items()))


