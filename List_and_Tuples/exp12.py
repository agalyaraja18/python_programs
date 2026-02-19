l=list(map(int,input().split()))
lst=list(set(l))
if len(lst)<2:
    print(-1)
else:
    second_l=sorted(lst)[-2]
    print(l.index(second_l))