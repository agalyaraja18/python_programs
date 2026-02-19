income=int(input("Enter the income:"))
credit_score=int(input("Enter the credit score (in range of 0-1000):"))
existing_debt=int(input("Enter the existing debt:"))
if income<=0:
    print("Reject")
dti=existing_debt/income
if credit_score>=750 and dti<=0.35:
    print("Eligible")
elif credit_score<650 and dti>0.05:
    print("Reject")
else:
    print("Review")