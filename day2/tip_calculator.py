print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
personCount = int(input("How many people to split the bill? "))

tip = bill * percentage / 100
billAfterTip = bill + tip
eachBill = billAfterTip / personCount

print(f"Each person should pay: ${round(eachBill, 2)}")
