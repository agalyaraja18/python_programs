from functools import reduce
prices = list(map(int,input("Enter the list of prices:").split()))
discounted = map(lambda x: x * 0.9, prices)
filtered = filter(lambda x: x >= 200, discounted)
total = reduce(lambda a, b: a + b, filtered, 0)
print("Final Bill Total:", total)