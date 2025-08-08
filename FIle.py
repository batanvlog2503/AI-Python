
import os
file_path = "test.txt"

if os.path.exists(file_path):
    print(f"File {file_path} exists")
else:
    print("not exists")

txt_data = "I Like Pizza"

file_path = "output.txt"
employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]
with open(file_path,"a") as file:
    for employee in employees:
        file.write(employee)
    # file.write(txt_data)
    # print(f"txt file {file_path} was created" )