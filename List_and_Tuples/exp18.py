nums=list(map(int,input("Enter the elements:").split()))
l=[]
max=0
for i in range(len(nums)):
    if nums[i]<=0:
        max=0
    else:
        if nums[i]>max:
            max=nums[i]
    l.append(max)
print(l)