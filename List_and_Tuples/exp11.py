l=list(input().split())
result = [(l[i], l[i+1]) for i in range(0, len(l) - 1, 2)]
print(result)