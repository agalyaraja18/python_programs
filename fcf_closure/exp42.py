def make_multiplier(k):
    def multiplier(x):
        return x * k
    return multiplier
double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))
print(triple(4))