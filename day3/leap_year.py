year = int(input("Which year do you want to check? "))
divisible_four = year % 4 == 0
divisible_hundred = year % 100 == 0
divisible_four_hundred = year % 400 == 0

if (divisible_four and not divisible_hundred) or divisible_four_hundred:
    print("Leap year.")
else:
    print("Not leap year.")
