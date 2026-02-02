income = input("Enter income (high/low): ").lower()
credit = input("Enter credit score (good/bad): ").lower()

if income == "high":
    print("Class: LOAN APPROVED")
elif credit == "good":
    print("Class: LOAN APPROVED")
else:
    print("Class: LOAN REJECTED")
