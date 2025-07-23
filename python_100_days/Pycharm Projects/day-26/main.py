import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_dataframe = pandas.DataFrame(student_dict)
print(student_dataframe)

# for (key, value) in student_dataframe.items():
#     print(value)

# Loop through each of the rows of a dataframe
for (index, row) in student_dataframe.iterrows():
    if row["student"] == "Angela":
        print(row["score"])