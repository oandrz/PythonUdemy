import pandas

'''
find count of primary fur color column
gray, cinnamon and black
'''

data = pandas.read_csv("./csv/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_group = data.groupby("Primary Fur Color")["Primary Fur Color"]
fur_dict = {
    "Fur Color": [],
    "Count": []
}
for group in fur_group:
    fur_dict["Fur Color"].append(group[0])
    fur_dict["Count"].append(group[1].count())
pandas.DataFrame(fur_dict).to_csv("./csv/squirrel_color_group_count")
