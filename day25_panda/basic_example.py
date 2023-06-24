import pandas
import csv

'''
Read CSV using CSV python builtin
'''
# with open("weather_data.csv") as file:
#     weather_data = csv.reader(file)
#     temperatures = []
#     for row in weather_data:
#         if row[1].isdigit():
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

'''
Conversion to list and dict
'''
data = pandas.read_csv("csv/weather_data.csv")
print(data)
print(data.to_dict()) # to dictionary

print(data["temp"])
print(data["temp"].tolist()) # to convert to python

'''
To get the average value
'''
temps = data["temp"].tolist()
avg_temp = sum(temps) / len(temps)
print(f"Average temp is {round(avg_temp, 2)}")

# Using panda
print(round(data["temp"].mean(), 2))

'''
Get max value
'''
print(data["temp"].max())

'''
get series
'''
print(data["condition"])
print(data.condition)

'''
get data based on row
'''
# Pull out data where day is monday
print(data[data.day == "Monday"])

# Get max data
print(data[data.temp == data.temp.max()])

'''
Get data on specific row and col
'''
monday = data[data.day == "Monday"]
print(monday.condition)
monday_temp = int(monday.temp[0])
monday_temp_farrenheit = monday_temp * 9/5 + 32
print(monday_temp_farrenheit)

'''
Create data frame from scratch
'''
data_dict = {
    "students": ["Dre"],
    "scores": [100]
}
student_data = pandas.DataFrame(data_dict)
print(student_data)
student_data.to_csv("new_data.csv")