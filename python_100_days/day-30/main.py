# try:
#     file = open("file.txt")
#     dictionary = {"key": "value"}
#     print(dictionary["key"])
# except FileNotFoundError:
#     # Opening a file in write mode creates it if it doesn't exist
#     file = open("file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     # This is run when there are no exceptions
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError("This is an error I made up")


height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / height ** 2

print(bmi)