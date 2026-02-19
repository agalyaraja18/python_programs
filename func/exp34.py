from functools import reduce
scores = list(map(int, input("Enter the scores:").split()))
weights = list(map(float, input("Enter the weights:").split()))
weighted_sum = reduce(
    lambda acc, sw: acc + (sw[0] * sw[1]),
    zip(scores, weights),
    0
)
total_weight = reduce(lambda a, b: a + b, weights, 0)
weighted_score = weighted_sum / total_weight
print("Weighted Score:", weighted_score)
