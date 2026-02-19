nums=list(map(int, input("Enter the elements:").split()))
result=[]
for num in nums:
    if num%2==0:
        result.append(num**2)
print(result)