amount=int(input("Enter amount:"))
if amount<1000:
    amount=amount
elif amount>=1000 and amount<5000:
    a=amount*0.05
    amount=amount-a
else:
    a=amount*0.1
    amount=amount-a
print("The payable amount is",amount)