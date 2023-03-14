height = float(input("enter your height in m: "))
weight = int(input("enter your weight in kg: "))
bmi = round(weight / height ** 2)
ceiledBmi = bmi
status = ""
if ceiledBmi < 18.5:
    status = "are underweight"
elif 18.5 <= ceiledBmi < 25:
    status = "have a normal weight"
elif 25 <= ceiledBmi < 30:
    status = "are slightly overweight"
elif 30 <= ceiledBmi < 35:
    status = "are obese"
else:
    status = "are clinically obese"

print(f"Your BMI is {ceiledBmi}, you {status}.")
