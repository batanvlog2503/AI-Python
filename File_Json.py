import json
import csv
employee = {
    "name" : "Spongebob",
    "age" : 30,
    "job" : "cook"

}

file_path = "output.json"

try:
    with open(file_path, "w") as file:
        # voi csv
        # writer = csv.writer(file)
        # for row in employees:
        #     writer.writerow(row)
        json.dump(employee, file, indent=4)
        print(f"Json file {file_path} was created")
except FileExistsError:
    print("That file already exists")