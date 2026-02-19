text=input("Enter a text:")
substring=input("Enter a substring:")
count=0
start=0
while True:
    start=text.find(substring,start)
    if start==-1:
        break
    count+=1
    start+=1
print("The substring overlaps count is",count)