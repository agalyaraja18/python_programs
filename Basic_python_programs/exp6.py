s=input("Enter a string with digits:")
d=[]
for i in range(len(s)):
    d.append(s[i])
ind=[]
for j in range(len(d)):
    if d[j] in "0123456789":
        ind.append(j)
for a in ind:
    d[a]="#"
print("".join(d))
