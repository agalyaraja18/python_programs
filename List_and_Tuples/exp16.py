nums=list(map(int,input("Enter the elements:").split()))
a=0
for num in nums:
    if num<0:
        break
    a+=num
print(a)