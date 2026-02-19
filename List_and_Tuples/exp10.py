l=list(map(int,input().split()))
s=set()
dl=[]
for i in range(len(l)):
    if l[i] not in s:
        s.add(l[i])
        dl.append(l[i])
print(dl)