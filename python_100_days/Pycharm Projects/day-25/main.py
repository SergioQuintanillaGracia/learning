# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temps = []
#
#     for row in data:
#         temp = row[1]
#
#         if temp != "temp":
#             temp = int(temp)
#             temps.append(temp)
#
#     print(temps)

import pandas

# data = pandas.read_csv("weather_data.csv")

# print(data)
# print(data["temp"])
# print(type(data))  # DataFrame (the whole table)
# print(type(data["temp"]))  # Series (list)

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# # avg = 0
# # for temp in temp_list:
# #     avg += temp / len(temp_list)
# # print(f"Average temperature: {avg}")
#
# print(f"Average temperature: {data["temp"].mean()}")
# print(f"Max temperature: {data["temp"].max()}")

# print(data.condition)  # This is the same as data["condition"]

# # Get data of a certain row
# print(data[data.day == "Monday"])
#
# max_temp = data.temp.max()
# print(f"Max temp row:\n{data[data.temp == max_temp]}")

# monday_row = data[data.day == "Monday"]
# monday_temp = monday_row.temp
# print(monday_temp)

# # Creating a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_col = data["Primary Fur Color"]
value_counts = fur_col.value_counts()

count_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [value_counts["Gray"], value_counts["Cinnamon"], value_counts["Black"]]
}

count_data = pandas.DataFrame(count_dict)
count_data.to_csv("squirrel_count.csv")
print(count_data)