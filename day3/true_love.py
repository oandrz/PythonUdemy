def text_calculator(text, table_param):
    count = 0
    for c in text:
        count += table_param[c]

    return count


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined = name1.lower() + name2.lower()
true_love_text = "truelove"

table = dict()
for c in true_love_text:
    table[c] = combined.count(c)

true_count = text_calculator("true", table)
love_count = text_calculator("love", table)
percentage = int(f"{true_count}{love_count}")

status = ""

if percentage < 10 or percentage > 90:
    status = ", you go together like coke and mentos"
elif 40 <= percentage <= 50:
    status = ", you are alright together"

print(f"Your score is {percentage}{status}.")
